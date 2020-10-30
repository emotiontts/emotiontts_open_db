"""

Seq2Seq G2P 모델 구현

@author: Jeongpil Lee (koreanfeel@gmail.com)
@created at : 2018. 03. 14.

"""
import os
import json
import tensorflow as tf
import numpy as np
from six import text_type
import re
import hgtk

from korean_g2p_code import conv_hangul_to_code, conv_code_to_hangul

_PAD = "--PAD--"
_UNK = "--UNK--"
_GO = "--START--"
_EOS = "--END--"
_SPACE = "_"
_START_VOCAB = [_PAD, _UNK, _GO, _EOS, _SPACE]


class Seq2Seq(object):
    def __init__(self, flags, encoder_word_embeddings, decoder_word_embeddings):
        self.flags = flags
        self.encoder_word_embeddings = encoder_word_embeddings
        self.decoder_word_embeddings = decoder_word_embeddings
        self.max_encoder_length = self.flags.max_encoder_length
        self.max_decoder_length = self.flags.max_decoder_length
        self.encoder_vocab_size = len(encoder_word_embeddings)
        self.decoder_vocab_size = len(decoder_word_embeddings)

        if self.flags.encoder_embedding_size == 0:
            self.encoder_embedding_size = self.encoder_vocab_size
        else:
            self.encoder_embedding_size = self.flags.encoder_embedding_size

        if self.flags.decoder_embedding_size == 0:
            self.decoder_embedding_size = self.decoder_vocab_size
        else:
            self.decoder_embedding_size = self.flags.decoder_embedding_size

        self.hidden_size = self.flags.hidden_size
        self.start_idx = self.flags.start_idx
        self.end_idx = self.flags.end_idx
        self.batch_size = self.flags.batch_size
        self.beam_width = self.flags.beam_width
        self.attention_hidden_size = self.flags.attention_hidden_size
        self.PAD_ID = self.flags.PAD_ID
        self.mode = self.flags.mode

        self._input_init()
        self._embedding_init()
        self._encoder_init()
        self._attention_init()
        self._decoder_init()
        self._predict_init()

    def _input_init(self):
        self.encoder_inputs = tf.compat.v1.placeholder(tf.int32, [self.batch_size, self.max_encoder_length],
                                                       "encoder_inputs")

        self.encoder_length = tf.reduce_sum(
            tf.cast(tf.not_equal(self.encoder_inputs, self.PAD_ID), dtype=tf.int32), 1,
            name="encoder_input_lengths")

    def _embedding_init(self):
        with tf.compat.v1.variable_scope("emb_var"), tf.device("/cpu:0"):
            self.encoder_embeddings = tf.compat.v1.get_variable("encoder_embeddings",
                                                                shape=[self.encoder_vocab_size,
                                                                       self.encoder_embedding_size],
                                                                dtype=tf.float32, trainable=True,
                                                                initializer=tf.constant_initializer(
                                                                    self.encoder_word_embeddings))
            self.decoder_embeddings = tf.compat.v1.get_variable("decoder_embeddings",
                                                                shape=[self.decoder_vocab_size,
                                                                       self.decoder_embedding_size],
                                                                dtype=tf.float32, trainable=True,
                                                                initializer=tf.constant_initializer(
                                                                    self.decoder_word_embeddings))

    def _encoder_init(self):
        with tf.compat.v1.variable_scope("encoder_layer"):
            encoder_lookup_inputs = tf.nn.embedding_lookup(self.encoder_embeddings, self.encoder_inputs)

            cell_fw = tf.contrib.rnn.LSTMCell(self.hidden_size)
            cell_bw = tf.contrib.rnn.LSTMCell(self.hidden_size)
            (fw_outputs, bw_outputs), (fw_state, bw_state) = tf.nn.bidirectional_dynamic_rnn(
                cell_fw=cell_fw, cell_bw=cell_bw, inputs=encoder_lookup_inputs,
                sequence_length=self.encoder_length, dtype=tf.float32, time_major=False)

            self.encoder_outputs = tf.concat([fw_outputs, bw_outputs], -1)
            self.encoder_output_state = tf.concat([fw_state[-1], bw_state[-1]], -1)

    def _attention_init(self):
        with tf.compat.v1.variable_scope("attention_layer"):
            if self.flags.decoder != 'basic':
                self.encoder_outputs = tf.contrib.seq2seq.tile_batch(self.encoder_outputs, self.beam_width)
                self.encoder_length = tf.contrib.seq2seq.tile_batch(self.encoder_length, self.beam_width)

            self.mechanism = tf.contrib.seq2seq.LuongAttention(num_units=self.attention_hidden_size,
                                                               memory=self.encoder_outputs,
                                                               memory_sequence_length=self.encoder_length)

    def _decoder_init(self):
        with tf.compat.v1.variable_scope("decode_layer"):
            cell = tf.contrib.rnn.LSTMCell(self.hidden_size * 2)
            cell = tf.contrib.seq2seq.AttentionWrapper(cell, self.mechanism,
                                                       attention_layer_size=self.attention_hidden_size,
                                                       alignment_history=False)
            cell = tf.contrib.rnn.OutputProjectionWrapper(cell, self.decoder_vocab_size)

            if self.flags.decoder == 'basic':
                init_state = cell.zero_state(self.batch_size, dtype=tf.float32)
            else:
                init_state = cell.zero_state(self.batch_size * self.beam_width, dtype=tf.float32)

            if self.flags.decoder == 'basic':
                print('BasicDecoder')
                helper = tf.contrib.seq2seq.GreedyEmbeddingHelper(self.decoder_embeddings,
                                                                  start_tokens=tf.fill([self.batch_size],
                                                                                       self.start_idx),
                                                                  end_token=self.end_idx)
                decoder = tf.contrib.seq2seq.BasicDecoder(cell, helper, init_state)
            else:
                decoder = tf.contrib.seq2seq.BeamSearchDecoder(cell=cell, embedding=self.decoder_embeddings,
                                                               start_tokens=tf.fill([self.batch_size],
                                                                                    self.start_idx),
                                                               end_token=self.end_idx, initial_state=init_state,
                                                               beam_width=self.beam_width)

            self.outputs, _, _ = tf.contrib.seq2seq.dynamic_decode(decoder=decoder,
                                                                   maximum_iterations=self.max_decoder_length)

    def _predict_init(self):
        with tf.compat.v1.variable_scope("predict"):
            if self.flags.decoder == 'basic':
                self.predict_op = self.outputs.sample_id
            else:
                self.predict_op = self.outputs.predicted_ids


def symbols_to_ids(symbols, vocab):
    """Turn symbols into ids sequence using given vocabulary file.

    Args:
      symbols: input symbols sequence;
      vocab: vocabulary (a dictionary mapping string to integers).

    Returns:
      ids: output sequence of ids.
    """
    ids = [vocab.get(s, _START_VOCAB.index(_UNK)) for s in symbols]
    return ids


def get_word():
    """Get next word in the interactive mode."""
    word = ""
    try:
        word = input("> ")
        if not issubclass(type(word), text_type):
            word = text_type(word, encoding="utf-8", errors="replace")
    except EOFError:
        pass
    if not word:
        pass
    return word


def split_sentences(text):
    outputs = []
    find_iter = re.finditer(r'(?<![_\s])[\?!.]', text)  # ?, !, . 을 기준으로 문장 분리

    last_end_pos = 0
    for match in find_iter:
        end_pos = match.span()[1]

        outputs.append(text[last_end_pos:end_pos].strip())
        last_end_pos = end_pos

    return outputs


def post_process(text):
    """
    무음가 초성, 종성 제거.

    :param text:
    :return:
    """
    tokens = text.split()
    outputs = []

    for token in tokens:
        if token not in ['-', '=']:  # - : 초성, = : 종성
            outputs.append(token)

    return ' '.join(outputs)


def decode(flags):
    #
    # 저장된 모델 파라미터를 불러와옴
    #
    params_path = os.path.join(flags.save_dir, 'params.json')

    if os.path.isfile(params_path):
        with open(params_path, "r", encoding='utf-8') as fp:
            params = json.load(fp)

        flags.max_encoder_length = params['max_encoder_length']
        flags.max_decoder_length = params['max_decoder_length']
        flags.encoder_embedding_size = params['encoder_embedding_size']
        flags.decoder_embedding_size = params['decoder_embedding_size']
        flags.hidden_size = params['hidden_size']
        flags.attention_hidden_size = params['attention_hidden_size']

    flags.batch_size = 1
    print_mode = flags.print_mode
    input_path = flags.in_path
    output_path = flags.out_path

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 현재 파라미터 값 출력
    print('\n### TEST Parameters ###')
    for key in flags:
        print('{} : {}'.format(key, flags[key].value))

    # Encoder Word Embedding 파일
    with open(flags.encoder_word_emb_file, "r") as fp:
        encoder_word_mat = np.array(json.load(fp), dtype=np.float32)

    # Decoder Word Embedding 파일
    with open(flags.decoder_word_emb_file, "r") as fp:
        decoder_word_mat = np.array(json.load(fp), dtype=np.float32)

    # Encoder index-to-word 파일
    with open(flags.encoder_idx2word_file, "r") as fp:
        encoder_idx2word = json.load(fp)

    # Decoder index-to-word 파일
    with open(flags.decoder_idx2word_file, "r") as fp:
        decoder_idx2word = json.load(fp)

    encoder_word2idx = dict([(x, y) for (y, x) in encoder_idx2word.items()])

    print("Building model...")

    model = Seq2Seq(flags, encoder_word_mat, decoder_word_mat)

    sess_config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
    sess_config.gpu_options.allow_growth = True

    with tf.compat.v1.Session(config=sess_config) as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        saver = tf.compat.v1.train.Saver()

        #
        # 모델 체크포인트 관련
        #
        checkpoint_state = tf.train.get_checkpoint_state(flags.save_dir)
        checkpoint_latest_path = checkpoint_state.model_checkpoint_path
        checkpoint_path = checkpoint_latest_path

        print('checkpoint_state :', checkpoint_state)
        print('latest checkpoint :', checkpoint_latest_path)
        print('current checkpoint :', checkpoint_path)

        saver.restore(sess, checkpoint_path)

        def list2str(idx2word_dict, input_list):
            temp_list = []
            for token_idx in input_list:
                if token_idx == flags.end_idx or token_idx == -1 or token_idx == flags.PAD_ID:
                    break
                token = idx2word_dict[str(token_idx)]
                temp_list.append(token)

            result_str = " ".join(temp_list)
            return result_str

        def decode_text(text):
            text = ' '.join(text.split())  # 띄어쓰기가 여러개인 경우 1개로 수정

            # 마지막 값에 문장부호 표시
            last_char = text[-1]
            if last_char not in ['?', '!']:
                last_char = '$'

            umjeol_list = [x for x in text.strip()]

            text = re.sub(r'[^가-힣 ]+', '', text)  # 한글 및 스페이스만 남겨두고 나머지는 제거
            text = conv_hangul_to_code(text, 'g')
            text = text.split()

            input_len = len(text)

            # 입력 데이터가 없을 경우에 대한 처리
            if input_len == 0:
                return str()

            gr_ids = symbols_to_ids(text, encoder_word2idx)

            encoder_inputs = np.zeros([flags.max_encoder_length], dtype=np.int32)

            for i, gr_id in enumerate(gr_ids):
                encoder_inputs[i] = gr_id

            encoder_inputs_tensor = tf.convert_to_tensor(encoder_inputs, dtype=tf.int32)
            encoder_input, predict = sess.run(
                [encoder_inputs_tensor, model.predict_op],
                feed_dict={model.encoder_inputs: [encoder_inputs]})

            if flags.decoder == 'basic':
                predict_str = list2str(decoder_idx2word, predict[0])
            else:
                predict_str = list2str(decoder_idx2word, predict[0][:, 0])

            predicted_len = len(predict_str.split())
            if predicted_len > input_len:
                predict_str_list = predict_str.split()
                predict_str = ' '.join(predict_str_list[:input_len])
            elif predicted_len < input_len:
                print('Error : predicted_len is shorter than input_len')
                return str()

            if print_mode == 'phoneme':
                out_str = predict_str + ' ' + last_char

            else:
                out_str = phonemes_to_hangul(predict_str, umjeol_list)

            return out_str

        if flags.mode == 'decode':
            file_count = 0
            for curdir, dirs, files in os.walk(input_path):
                for file in sorted(os.listdir(curdir)):
                    print('current file :', file)
                    filename, file_extension = os.path.splitext(os.path.basename(file))

                    if file_extension != '.txt':  # .txt 파일에 대해서만 처리
                        continue

                    outputs = []
                    with open(os.path.join(curdir, file), 'r', encoding='utf-8') as f:

                        for line in f:
                            line = line.strip()

                            sents = split_sentences(line)

                            if len(sents) == 0:
                                sents.append(line)

                            output_seqs = []
                            for sent in sents:
                                phoneme = decode_text(sent.strip())
                                phoneme = post_process(phoneme)

                                output_seqs.append(phoneme)

                            outputs.append(' '.join(output_seqs))

                    new_filename = filename + '.lbl'
                    with open(os.path.join(output_path, new_filename), 'w', encoding='utf-8') as f:
                        for line in outputs:
                            f.write(line + '\n')

                    file_count += 1

            print('\nInput path :', input_path)
            print('Output path :', output_path)
            print('Finished! Total converted files :', file_count)

        elif flags.mode == 'interactive':
            while True:
                try:
                    word = get_word()

                    if len(word) == 0:
                        print('INFO: 입력된 문장이 없습니다.')
                        continue

                    print(decode_text(word))

                except Exception as e:
                    import traceback
                    print(e)
                    print(traceback.print_exc())
        else:
            print("Unknown mode")
            exit(0)


def phonemes_to_hangul(predict_str, umjeol_list):
    out_str = ''
    p_text = conv_code_to_hangul(predict_str, g_or_p='p')

    #
    # 한글 이외의 문자는 입력텍스트와 동일하게 출력
    #
    i = 0
    is_space = False  # 스페이스가 연속적으로 나올 경우를 처리하기 위한 변수
    is_start = False  # 한글이 처음 나왔을 때 True로 변경
    for umjeol in umjeol_list:
        if hgtk.checker.is_hangul(umjeol):
            out_str += p_text[i]
            i += 1
            is_space = False
            is_start = True
        elif umjeol == ' ':
            if not is_space and is_start:
                out_str += umjeol
                i += 1
                is_space = True
            else:
                out_str += umjeol
        else:
            out_str += umjeol

    return out_str


def main(_):
    flags = tf.flags.FLAGS
    decode(flags)


if __name__ == "__main__":
    model_path = "model"

    encoder_word_emb_file = os.path.join(model_path, "encoder_word_emb.json")
    decoder_word_emb_file = os.path.join(model_path, "decoder_word_emb.json")
    encoder_idx2word_file = os.path.join(model_path, "encoder_idx2word.json")
    decoder_idx2word_file = os.path.join(model_path, "decoder_idx2word.json")

    tf.app.flags.DEFINE_string("mode", "interactive", "Running mode interactive/decode")
    tf.app.flags.DEFINE_string("in_path", "input", "Input path")
    tf.app.flags.DEFINE_string("out_path", "output", "Input path")
    tf.app.flags.DEFINE_string("print_mode", "hangul", "hangul/phoneme")
    tf.app.flags.DEFINE_string("decoder", "beamsearch", "basic/beamsearch")

    tf.app.flags.DEFINE_string("encoder_word_emb_file", encoder_word_emb_file, "encoder_word_emb_file")
    tf.app.flags.DEFINE_string("decoder_word_emb_file", decoder_word_emb_file, "decoder_word_emb_file")
    tf.app.flags.DEFINE_string("encoder_idx2word_file", encoder_idx2word_file, "encoder_idx2word_file")
    tf.app.flags.DEFINE_string("decoder_idx2word_file", decoder_idx2word_file, "decoder_idx2word_file")
    tf.app.flags.DEFINE_string("save_dir", model_path, "save_dir")

    tf.app.flags.DEFINE_integer("max_encoder_length", 440, "max_encoder_length")
    tf.app.flags.DEFINE_integer("max_decoder_length", 440, "max_decoder_length")
    tf.app.flags.DEFINE_integer("encoder_embedding_size", 50, "encoder_embedding_size")
    tf.app.flags.DEFINE_integer("decoder_embedding_size", 50, "decoder_embedding_size")
    tf.app.flags.DEFINE_integer("hidden_size", 100, "hidden_size")
    tf.app.flags.DEFINE_integer("start_idx", 2, "start_idx")
    tf.app.flags.DEFINE_integer("end_idx", 3, "end_idx")
    tf.app.flags.DEFINE_integer("PAD_ID", 0, "PAD_ID")
    tf.app.flags.DEFINE_integer("UNK_ID", 1, "UNK_ID")
    tf.app.flags.DEFINE_integer("attention_hidden_size", 200, "attention_hidden_size")
    tf.app.flags.DEFINE_integer("beam_width", 10, "beam_width")
    tf.app.flags.DEFINE_integer("batch_size", 512, "batch_size")

    tf.compat.v1.app.run()
