#!/bin/bash

# Copyright 2018 Nagoya University (Tomoki Hayashi)
# [stage 6] 2019 Okayama University (Katsuki Inoue)
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

. ./path.sh || exit 1;
. ./cmd.sh || exit 1;

# general configuration
backend=pytorch
stage=-1
stop_stage=100
ngpu=1       # number of gpus ("0" uses cpu, otherwise use gpu)
gpu=0
nj=32        # numebr of parallel jobs
dumpdir=dump # directory to dump full features
verbose=1    # verbose option (if set > 0, get more log)
N=0          # number of minibatches to be used (mainly for debugging). "0" uses all minibatches.
seed=1       # random seed number
resume=""    # the snapshot path to resume (if set empty, no effect)

# feature extraction related
fs=22050      # sampling frequency
fmax=7600     # maximum frequency
fmin=80       # minimum frequency
n_mels=80     # number of mel basis
n_fft=1024    # number of fft points
n_shift=256   # number of shift points
win_length="" # window length

# char or phn
# In the case of phn, input transcription is convered to phoneem using https://github.com/Kyubyong/g2p.
trans_type="char"

# config files
train_config=conf/tuning/train_pytorch_transformer.v3.single.yaml   # you can select from conf or conf/tuning.
                                                                    # now we support tacotron2, transformer, and fastspeech
                                                                    # see more info in the header of each config.
decode_config=conf/decode.yaml

# knowledge distillation related
teacher_model_path=""
teacher_decode_config=conf/decode_for_knowledge_dist.yaml
do_filtering=false     # whether to do filtering using focus rate
focus_rate_thres=0.65  # for phn taco2 around 0.65, phn transformer around 0.9
                       # if you want to do filtering please carefully check this threshold

# decoding related
model=model.loss.best
n_average=1 # if > 0, the model averaged with n_average ckpts will be used instead of model.loss.best
griffin_lim_iters=64  # the number of iterations of Griffin-Lim

# objective evaluation related
asr_model="librispeech.transformer.ngpu4"
eval_tts_model=true                            # true: evaluate tts model, false: evaluate ground truth
wer=true                                       # true: evaluate CER & WER, false: evaluate only CER

# root directory of db
db_root=/data/DB/emotiontts_open_db/Main/main/lmy

# exp tag
tag_data="" # tag for managing feature data.
tag_model="" # tag for managing models.

. utils/parse_options.sh || exit 1;

# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

train_set="${trans_type}_train_no_dev"
dev_set="${trans_type}_dev"
eval_set="${trans_type}_eval"

# if [ ${stage} -le -1 ] && [ ${stop_stage} -ge -1 ]; then
    # echo "stage -1: Data Download"
    # local/data_download.sh ${db_root}
# fi

if [ -z ${tag_data} ]; then
    datadir=data
    dumpdir=dump
else
    datadir=data_${tag_data}
    dumpdir=dump_${tag_data}
fi

if [ ${stage} -le 0 ] && [ ${stop_stage} -ge 0 ]; then
    ### Task dependent. You have to make data the following preparation part by yourself.
    ### But you can utilize Kaldi recipes in most cases
    echo "stage 0: Data preparation"
    local/data_prep.sh ${db_root} ${datadir}/${trans_type}_train ${trans_type}
    utils/validate_data_dir.sh --no-feats ${datadir}/${trans_type}_train
fi

feat_tr_dir=${dumpdir}/${train_set}; mkdir -p ${feat_tr_dir}
feat_dt_dir=${dumpdir}/${dev_set}; mkdir -p ${feat_dt_dir}
feat_ev_dir=${dumpdir}/${eval_set}; mkdir -p ${feat_ev_dir}
if [ ${stage} -le 1 ] && [ ${stop_stage} -ge 1 ]; then
    ### Task dependent. You have to design training and dev name by yourself.
    ### But you can utilize Kaldi recipes in most cases
    echo "stage 1: Feature Generation"

    # Generate the fbank features; by default 80-dimensional fbanks on each frame
    if [ -z ${tag_data} ]; then
        fbankdir=fbank
        makefbankdir=${trans_type}_make_fbank
        dumpfeats=dump_feats
    else
        fbankdir=fbank_${tag_data}
        makefbankdir=${trans_type}_make_fbank_${tag_data}
        dumpfeats=dump_feats_${tag_data}
    fi

    make_fbank.sh --cmd "${train_cmd}" --nj ${nj} \
        --fs ${fs} \
        --fmax "${fmax}" \
        --fmin "${fmin}" \
        --n_fft ${n_fft} \
        --n_shift ${n_shift} \
        --win_length "${win_length}" \
        --n_mels ${n_mels} \
        ${datadir}/${trans_type}_train \
        exp/${makefbankdir}/train \
        ${fbankdir}

    # make a dev set (500, 250, 250) --> (130, 65, 65)
    utils/subset_data_dir.sh --last ${datadir}/${trans_type}_train 130 ${datadir}/${trans_type}_deveval
    utils/subset_data_dir.sh --last ${datadir}/${trans_type}_deveval 65 ${datadir}/${eval_set}
    utils/subset_data_dir.sh --first ${datadir}/${trans_type}_deveval 65 ${datadir}/${dev_set}
    n=$(( $(wc -l < ${datadir}/${trans_type}_train/wav.scp) - 130 ))
    utils/subset_data_dir.sh --first ${datadir}/${trans_type}_train ${n} ${datadir}/${train_set}

    # compute statistics for global mean-variance normalization
    compute-cmvn-stats scp:${datadir}/${train_set}/feats.scp ${datadir}/${train_set}/cmvn.ark

    # dump features for training
    dump.sh --cmd "$train_cmd" --nj ${nj} --do_delta false \
        ${datadir}/${train_set}/feats.scp ${datadir}/${train_set}/cmvn.ark exp/${dumpfeats}/${trans_type}_train ${feat_tr_dir}
    dump.sh --cmd "$train_cmd" --nj ${nj} --do_delta false \
        ${datadir}/${dev_set}/feats.scp ${datadir}/${train_set}/cmvn.ark exp/${dumpfeats}/${trans_type}_dev ${feat_dt_dir}
    dump.sh --cmd "$train_cmd" --nj ${nj} --do_delta false \
        ${datadir}/${eval_set}/feats.scp ${datadir}/${train_set}/cmvn.ark exp/${dumpfeats}/${trans_type}_eval ${feat_ev_dir}
fi

dict=${datadir}/lang_1${trans_type}/${train_set}_units.txt
echo "dictionary: ${dict}"
if [ ${stage} -le 2 ] && [ ${stop_stage} -ge 2 ]; then
    ### Task dependent. You have to check non-linguistic symbols used in the corpus.
    echo "stage 2: Dictionary and Json Data Preparation"
    mkdir -p ${datadir}/lang_1${trans_type}/
    echo "<unk> 1" > ${dict} # <unk> must be 1, 0 will be used for "blank" in CTC
    text2token.py -s 1 -n 1 --trans_type ${trans_type} ${datadir}/${train_set}/text | cut -f 2- -d" " | tr " " "\n" \
    | sort | uniq | grep -v -e '^\s*$' | awk '{print $0 " " NR+1}' >> ${dict}
    wc -l ${dict}

    # make json labels
    data2json.sh --feat ${feat_tr_dir}/feats.scp --trans_type ${trans_type} \
         ${datadir}/${train_set} ${dict} > ${feat_tr_dir}/data.json
    data2json.sh --feat ${feat_dt_dir}/feats.scp --trans_type ${trans_type} \
         ${datadir}/${dev_set} ${dict} > ${feat_dt_dir}/data.json
    data2json.sh --feat ${feat_ev_dir}/feats.scp --trans_type ${trans_type} \
         ${datadir}/${eval_set} ${dict} > ${feat_ev_dir}/data.json
fi


if [ -z ${tag_data} ] && [ -z ${tag_model} ]; then
    expname=${train_set}_${backend}_$(basename ${train_config%.*})
else
    expname=${train_set}_${backend}_$(basename ${train_config%.*})_${tag_data}_${tag_model}
fi
expdir=exp/${expname}
mkdir -p ${expdir}
if [ ${stage} -le 3 ] && [ ${stop_stage} -ge 3 ]; then
    echo "stage 3: Text-to-speech model training"
    if [ -n "${teacher_model_path}" ] && echo "${train_config}" | grep -q "fastspeech"; then
        # setup feature and duration for fastspeech knowledge distillation training
        teacher_expdir=$(dirname "$(dirname "${teacher_model_path}")")
        teacher_outdir=outputs_$(basename ${teacher_model_path})_$(basename ${teacher_decode_config%.*})
        teacher_outdir=${teacher_expdir}/${teacher_outdir}
        if [ ! -e ${teacher_outdir}/.done ]; then
            local/setup_knowledge_dist.sh \
                --nj ${nj} \
                --dumpdir ${dumpdir} \
                --datadir ${datadir} \
                --verbose ${verbose} \
                --dict ${dict} \
                --trans_type ${trans_type} \
                --teacher_model_path ${teacher_model_path} \
                --decode_config ${teacher_decode_config} \
                --train_set ${train_set} \
                --dev_set ${dev_set} \
                --do_filtering ${do_filtering} \
                --focus_rate_thres ${focus_rate_thres}
        fi
        tr_json=${teacher_outdir}/dump/${train_set}/data.json
        dt_json=${teacher_outdir}/dump/${dev_set}/data.json
    else
        tr_json=${feat_tr_dir}/data.json
        dt_json=${feat_dt_dir}/data.json
    fi
    ${cuda_cmd} --gpu ${ngpu} ${expdir}/train.log \
        CUDA_VISIBLE_DEVICES=${gpu} tts_train.py \
           --backend ${backend} \
           --ngpu ${ngpu} \
           --minibatches ${N} \
           --outdir ${expdir}/results \
           --tensorboard-dir tensorboard/${expname} \
           --verbose ${verbose} \
           --seed ${seed} \
           --resume ${resume} \
           --train-json ${tr_json} \
           --valid-json ${dt_json} \
           --config ${train_config}
fi

if [ ${n_average} -gt 0 ]; then
    model=model.last${n_average}.avg.best
fi
