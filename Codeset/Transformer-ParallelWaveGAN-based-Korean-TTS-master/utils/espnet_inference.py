import numpy as np
import torch
import argparse
import time
import os
import json
import yaml
import parallel_wavegan.models
import sys
sys.path.append("/home/administrator/espnet")
from espnet.asr.asr_utils import get_model_conf
from espnet.asr.asr_utils import torch_load
from espnet.utils.dynamic_import import dynamic_import
from espnet.nets.pytorch_backend.transformer.plot import _plot_and_save_attention
from text import text_to_sequence
from scipy.io import wavfile

def main():
    device = torch.device("cuda")
    torch.manual_seed(1)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # Define the seq2seq model
    model_dir = "/home/administrator/espnet/egs/tmp/tts1/exp/char_train_no_dev_pytorch_train_pytorch_transformer.v3.single/"
    model_path = os.path.join(model_dir, "results/model.loss.best")
    idim, odim, train_args = get_model_conf(model_path)
    print(f"Input dimension: {idim}, output dimension: {odim}")

    model_class = dynamic_import(train_args.model_module)
    model = model_class(idim, odim, train_args)
    torch_load(model_path, model)
    model = model.eval().to(device)
    inference_args = argparse.Namespace(
        **{
            "threshold": 0.5,
            "minlenratio": 0.0,
            "maxlenratio": 10.0,
            # Only for Tacotron 2
            "use_attention_constraint": True,
            "backward_window": 1,
            "forward_window": 3,
            # Only for fastspeech (lower than 1.0 is faster speech, higher than 1.0 is slower speech)
            "fastspeech_alpha": 1.0,
        }
    )

    # Define ParallelWaveGAN
    pwgan_path = (
        "/home/administrator/espnet/utils/parallelwavegan/checkpoints/checkpoint-1000000steps.pkl"
    )
    pwgan_conf = "/home/administrator/espnet/utils/parallelwavegan/config.yml"
    with open(pwgan_conf) as f:
        config = yaml.load(f, Loader=yaml.Loader)
    vocoder_class = config.get("generator_type", "ParallelWaveGANGenerator")
    vocoder = getattr(parallel_wavegan.models, vocoder_class)(
        **config["generator_params"]
    )
    vocoder.load_state_dict(
        torch.load(pwgan_path, map_location="cpu")["model"]["generator"]
    )
    vocoder.remove_weight_norm()
    vocoder.eval()
    pad_fn = torch.nn.ReplicationPad1d(
        config["generator_params"].get("aux_context_window", 0)
    )
    use_noise_input = vocoder_class == "ParallelWaveGANGenerator"
    if config["generator_params"]["out_channels"] > 1:
        from parallel_wavegan.layers import PQMF

        pqmf = PQMF(config["generator_params"]["out_channels"]).to(device)
    vocoder = vocoder.cuda()
            
    # Define the dictionary
    if model_dir.find("char") != -1:
        trans_type = "char"
        dict_path = "/home/administrator/espnet/egs/tmp/tts1/data/lang_1char/char_train_no_dev_units.txt"
    elif model_dir.find("phn") != -1:
        trans_type = "phn"
        dict_path = "/home/administrator/espnet/egs/tmp/tts1/data/lang_1phn/phn_train_no_dev_units.txt"

    with open(dict_path, encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.replace("\n", "").split(" ") for line in lines]
    char_to_id = {c: int(i) for c, i in lines}
    id_to_char = {int(i): c for c, i in lines}

    # Get input texts
    input_texts = [
        "트랜스포머와 패럴렐 웨이브갠 기반 엔드투엔드 음성합성기 데모입니다.",
        "원하는 문장을 입력하세요.",
    ]

    total_time = 0
    syn_time = 0
    idx = 0
    with torch.no_grad():
        for input_text in input_texts:
            start1 = time.time()

            # text-to-sequence
            idseq = np.array(
                text_to_sequence(input_text, char_to_id, "korean_cleaners")
            )
            idseq = torch.autograd.Variable(torch.from_numpy(idseq)).cuda().long()

            # Transformer inference
            start2 = time.time()
            y_pred, _, attn = model.inference(idseq, inference_args)
            print("mel_outputs and attentions are of {} and {}".format(y_pred.shape, attn.shape))  # [T_out, 80] & [# layers, # heads, T_out, T_in]

            # define function for plot prob and att_ws
            def _plot_and_save(array, figname, figsize=(6, 4), dpi=150):
                import matplotlib.pyplot as plt

                shape = array.shape
                if len(shape) == 1:
                    # for eos probability
                    plt.figure(figsize=figsize, dpi=dpi)
                    plt.plot(array)
                    plt.xlabel("Frame")
                    plt.ylabel("Probability")
                    plt.ylim([0, 1])
                elif len(shape) == 2:
                    # for tacotron 2 attention weights, whose shape is (out_length, in_length)
                    plt.figure(figsize=figsize, dpi=dpi)
                    plt.imshow(array, aspect="auto")
                    plt.xlabel("Input")
                    plt.ylabel("Output")
                elif len(shape) == 4:
                    # for transformer attention weights,
                    # whose shape is (#leyers, #heads, out_length, in_length)
                    plt.figure(figsize=(figsize[0] * shape[0], figsize[1] * shape[1]), dpi=dpi)
                    for idx1, xs in enumerate(array):
                        for idx2, x in enumerate(xs, 1):
                            plt.subplot(shape[0], shape[1], idx1 * shape[1] + idx2)
                            plt.imshow(x, aspect="auto")
                            plt.xlabel("Input")
                            plt.ylabel("Output")
                else:
                    raise NotImplementedError("Support only from 1D to 4D array.")
                plt.tight_layout()
                if not os.path.exists(os.path.dirname(figname)):
                    # NOTE: exist_ok = True is needed for parallel process decoding
                    os.makedirs(os.path.dirname(figname), exist_ok=True)
                plt.savefig(figname)
                plt.close()
            # attention plot
            attnname=os.path.join(model_dir, "attention_{}.png".format(idx))
            _plot_and_save(attn.cpu().numpy(), attnname)

            # synthesize
            audio_pred = vocoder.inference(y_pred).view(-1)
            audio = audio_pred.cpu().numpy()
            audio *= 32767 / max(0.01, np.max(np.abs(audio)))
            wavfile.write(
                os.path.join(
                    model_dir, "sample_{}.wav".format(idx)
                ),
                22050,
                audio.astype(np.int16),
            )
            total_time += time.time() - start1
            idx += 1
            syn_time += audio.size / 22050
    print(f"Generated {idx} waveforms that correspond to {syn_time} seconds in {total_time} seconds.")

if __name__ == "__main__":
    main()
