import argparse
import os
import soundfile as sf
import pretty_midi
import csv
from os import path
from tqdm import tqdm


FILE_TREE = {'wav': '.wav', 'mid': '.mid', 'txt': '.txt', 'lyric': '.txt', 'csv': '.csv'}
LANGUAGES = ['korean', 'english']
NUM_AUDIO = 50
MAX_LENGTH_DIFF = 5 # in sec
PHONE_KR = ['g', 'kk', 'n', 'd', 'tt', 'r', 'l', 'm', 'b', 'pp', 's', 
            'ss', 'ng', 'j', 'jj', 'ch', 'k', 't', 'p', 'h', 'y', 'w',
            'a', 'ae', 'eo', 'e', 'o', 'u', 'eu', 'ui', 'i', 'oe']
PHONE_EN = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's',
            't', 'v', 'w', 'z', 'zh', 'ch', 'sh', 'th', 'dh', 'ng', 'y',
            'ae', 'ei', 'e', 'ii', 'i', 'ai', 'a', 'ou',
            'u', 'ao', 'uu', 'oi', 'au', 'eo', 'er', 'oo']


class character:
    BulletDot = u'\u2022'
    CheckMark = u'\u2714'
    CrossMark = u'\u2717'
    Bold = '\033[1m'
    Red = '\u001b[31m'
    Yellow = '\033[93m'
    Green = '\u001b[32m'
    Blue = '\u001b[34m'
    LRed = '\033[91m'
    LGreen = '\033[92m'
    LBlue = '\033[94m'
    Reset = '\x1b[0m'


class CSVLabel:
    def __init__(self, line):
        self.start = float(line[0])
        self.end = float(line[1])
        self.pitch = int(line[2])
        self.syllable = line[3]


class TestResult:
    def __init__(self):
        self.path_exists = {key: False for key in FILE_TREE}
        self.file_list = []
        self.file_exists = {}
        self.phone_validity = {}
        self.label_validity = {}
        self.length_validity = {}


def load_audio(filename):
    audio, samplerate = sf.read(filename)
    length = len(audio)/samplerate

    return audio, length


def load_midi(filename):
    midi_data = pretty_midi.PrettyMIDI(filename)
    if len(midi_data.instruments) > 1:
        raise AssertionError(f"More than 1 track detected in {filename}")

    return midi_data.instruments[0].notes


def load_text(filename):
    text = open(filename).read()
    text = ' '.join(text.split())

    graph = text.split(' ')
    if graph[-1] == '':
        graph = graph[:-1]

    return graph


def load_label(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader, None)

        label = []
        for line in csv_reader:
            label.append(CSVLabel(line))

    return label


def test_file_exists(file_dict):
    test_result = True
    for key in file_dict:
        if not path.exists(file_dict[key]):
            test_result = False
            break

    return test_result


def test_phone_validity(text, language):
    test_result = True
    if language == 'korean':
        phone_list = PHONE_KR
    elif language == 'english':
        phone_list = PHONE_EN

    for syllable in text:
        for phone in syllable.split('_'):
            if phone not in phone_list:
                test_result = False

    return test_result


def test_label_validity(midi, text, label):
    test_result = True
    if len(midi) != len(text):
        test_result = False
    if len(midi) != len(label):
        test_result = False

    return test_result


def test_length_validity(midi, length):
    test_result = True
    if abs(length - midi[-1].end) > MAX_LENGTH_DIFF:
        test_result = False

    return test_result


def bool2mark(validity):
    if validity == True:
        mark = character.Bold + character.LGreen + character.CheckMark + character.Reset
    elif validity == False:
        mark = character.Bold + character.LRed + character.CrossMark + character.Reset

    return mark


def get_num_true(test_result):
    return sum(list(test_result.values()))


def print_test_description():
    print(
        '[CSD Test]',
        '- Test A: Accompaniment file existance test.',
        '- Test B: Phonemes in txt folder validation test.',
        '- Test C: Label file validation test.',
        '- Test D: Length validation test between an audio file and a MIDI file.', sep='\n')


def print_result_table(test_result, num_row=5):
    print(
        num_row*'-------------------|',
        num_row*'|  File  | A B C D |',
        num_row*'|------------------|', sep='\n')
    
    multi_row = []
    for i, filename in enumerate(test_result.file_list):
        file_exists = bool2mark(test_result.file_exists[filename])
        phone_validity = bool2mark(test_result.phone_validity[filename])
        label_validity = bool2mark(test_result.label_validity[filename])
        length_validity = bool2mark(test_result.length_validity[filename])

        single_row = f' {filename:6} | {file_exists} {phone_validity} {label_validity} {length_validity} '
        multi_row.append(single_row)
        if len(multi_row) >= num_row or i == len(test_result.file_list) - 1:
            print('|' + '||'.join(multi_row) + '|')
            multi_row = []

    print(num_row*'--------------------')


def print_total_result(test_result):
    print('[Test Result]')

    test_list = {'A': 'file_exists', 'B': 'phone_validity', 'C': 'label_validity', 'D': 'length_validity'}
    num_true = dict()
    total_result = dict()
    for test_key in test_list:
        test_val = test_list[test_key]
        num_true[test_val] = get_num_true(getattr(test_result, test_val))
        total_result[test_val] = bool2mark(num_true[test_val] == len(test_result.file_list))

        print(f'- Test {test_key}: {total_result[test_val]} ({num_true[test_val]}/{len(test_result.file_list)})')


def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main(args):
    print_test_description()

    test_result = TestResult()
    for i, language in enumerate(LANGUAGES):
        data_path = {key: path.join(args.path, language, key) for key in FILE_TREE}
        for key in data_path:
            test_result.path_exists[key] = path.exists(data_path[key])
        
        progress_bar = tqdm(sorted(os.listdir(data_path['wav'])), leave=False, bar_format='{l_bar}{bar:30}{r_bar}')
        for filename in progress_bar:
            filename = path.splitext(filename)[0]
            progress_bar.set_description(filename)
            test_result.file_list.append(filename)

            file_dict = {key: path.join(data_path[key], filename + FILE_TREE[key]) for key in FILE_TREE}
            test_result.file_exists[filename] = test_file_exists(file_dict)
            
            audio, length = load_audio(file_dict['wav'])
            midi = load_midi(file_dict['mid'])
            text = load_text(file_dict['txt'])
            label = load_label(file_dict['csv'])

            test_result.phone_validity[filename] = test_phone_validity(text, language)
            test_result.label_validity[filename] = test_label_validity(midi, text, label)
            test_result.length_validity[filename] = test_length_validity(midi, length)

    if args.print_result_table:
        print_result_table(test_result, num_row=args.num_row)
    print_total_result(test_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='The path of CSD')
    parser.add_argument('--num_row', type=int, default=5)
    parser.add_argument('--print_result_table', type=str2bool, default=True)
    parser.add_argument('--print_note_range', type=str2bool, default=True)
    parser.add_argument('--print_max_note_length', type=str2bool, default=True)
    args = parser.parse_args()

    main(args)