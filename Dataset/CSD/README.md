# CSD: Children's Song Dataset for Singing Voice Research
This repository contains detailed information about [Children's Song Dataset (CSD)](https://program.ismir2020.net/static/lbd/ISMIR2020-LBD-435-abstract.pdf). The official dataset is released via Zenodo in this [link](https://zenodo.org/record/4785016#.YLYW6P0QtTa).

CSD is open source dataset for singing voice research. This dataset contains 50 Korean and 50 English songs sung by one Korean female professional pop singer. Each song is recorded in two separate keys resulting in a total of 200 audio recordings. Each audio recording is paired with a MIDI transcription and lyrics annotations in both grapheme level and phoneme level.

1. [Dataset Structure](#dataset_structure)
2. [Vocal Recording](#vocal_recording)
3. [MIDI Transcription](#midi_transcription)
4. [Lyric Annotation](#lyric_annotation)
5. [Supplementary Code](#supplementary_code)
6. [License](#license)
7. [Download](#download)


## 1. Dataset Structure <a name="dataset_structure"></a>
The entire data splits into Korean and English and each language splits into 'wav', 'mid', 'lyric', 'txt' and 'csv' folders. Each song has the identical file name for each format. Each format represents following information. Additional information like original song name, tempo and time signature for each song can be found in 'metadata.json'.

```
(CSD)
├── english
│   ├── wav
│   ├── mid
│   ├── lyric
│   ├── txt
│   └── csv
└── korean
    ├── wav
    ├── mid
    ├── lyric
    ├── txt
    └── csv
```

- 'wav': Vocal recordings in 44.1kHz 16bit wav format
- 'mid': Score information in MIDI format
- 'lyric': Lyric information in grapheme level
- 'txt': Lyric information in syllable and phoneme level
- 'csv': Note onset and offset and syllable timing in comma-separated value (CSV) format

## 2. Vocal Recording <a name="vocal_recording"></a>
Children’s songs usually have various versions in different styles and one of them that suites for the singer is chosen. While recording vocals, the singer sang along with the background music tracks. She deliberately rendered the singing in a “plain” style refraining from expressive singing skills. The recording took place in a dedicated soundproof room. Singer recorded three to four takes for each song and the best parts are combined into a single audio track. Two identical songs with different keys are discriminated by character 'a' and 'b' at the end of a filename.

## 3. MIDI Transcription <a name="midi_transcription"></a>
The MIDI data consists of monophonic notes. Each note contains onset and offset times which were manually fine-tuned along with the corresponding syllable. MIDI notes do not include any expression data or control change messages because those parameters can be ambiguous to define for singing voice. Singing voice is an highly expressive sound and so it is hard to define precise onset timings and pitches. We assumed one syllable matches with one MIDI note and made the following criteria to represent various expressions in singing voice.

- A piano sound is used as a reference tone for the annotated MIDI to ensure the alignment with vocal.
- The rising pitch at the beginning of a note is included within a single note.
- The end of syllable is treated as the offset of a note.
- The breathing sound during short pauses is not treated as note onset or offset.
- Vibrato is treated as a single sustaining note.
- If a syllable is rendered with several different pitches, we annotated them as separate notes.

## 4. Lyric Annotation <a name="lyric_annotation"></a>
Text files represent pronunciation for the corresponding audio. We did not include phonetic alignment because the MIDI notes can be used for syllable timings. Text files in the 'lyric' folder contains raw text for corresponding audio and the 'txt' folder contains phoneme-level lyric representation. The phoneme-level lyric representation is annotated in a special text format. Phonemes in a syllable are tied with underbar('_') and syllables are separated with space(' ') as the example below.

In the 'lyric' folder
```
twinkle twinkle little star
```

In the 'text' folder
```
t_w_i_ng k_eo_l t_w_i_ng k_eo_l l_i t_eo_l s_t_a_r
```

Each phonemes are annotated based on the international phonetic alphabet (IPA) and romanized alphabets are used to annotate IPA symbols. Following symbols are used for phoneme annotation.

### English
|Consonant  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|-----------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| Phoneme   |b |d |f |g |h |j |k |l |m |n |p |r |s |t |v |w |
| IPA       |b |d |f |g |h |dʒ|k |l |m |n |p |r |s |t |v |w |
| Phoneme   |z |zh|ch|sh|th|dh|ng|y |  |  |  |  |  |  |  |  |
| IPA       |z |ʒ |tʃ|ʃ |θ |ð |ŋ |j |  |  |  |  |  |  |  |  |


| Vowel     |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|-----------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| Phoneme   |ae|ei|e |ii|i |ai|a |ou|u |ao|uu|oi|au|eo|er|oo|
| IPA       |æ |eɪ|e |i:|h |dʒ|k |l |m |n |p |r |s |t |v |w |

### Korean
| Consonant |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|-----------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|---|
| Phoneme   |g |kk|n |d |tt|r |l |m |b |pp|s |ss|ng|j |jj|ch |
| IPA       |g |k͈ |n |d |t͈ |ɾ |l |m |b |p͈ |s |s͈ |ŋ |ts|ts͈|tsʰ|
| Phoneme   |k |t |p |h |y |w |  |  |  |  |  |  |  |  |  |   |
| IPA       |k |t |p |h |j |w |  |  |  |  |  |  |  |  |  |   |


| Vowel     |  |  |  |  |  |  |  |  |  |
|-----------|--|--|--|--|--|--|--|--|--|
| Phoneme   |a |ae|eo|e |o |u |eu|ui|i |
| IPA       |a |ɛ |ʌ |e |o |u |ɯ |ɰi|i |


## 5. Supplementary Code <a name="supplementary_code"></a>
This repository also offers dataset validation test code and example code for loading MIDI and text file. To test the dataset run the following command:
```
python test.py --data_path ./
```

If there are not problem found in the dataset, you will get the result as below.
```
[Test Result]
- Test A: ✔ (200/200)
- Test B: ✔ (200/200)
- Test C: ✔ (200/200)
- Test D: ✔ (200/200)
[MIDI Summary]
Note Range: 54 ~ 76, Max Note Length: 0.450s
```
When loading MIDI or text file you can also refer to 'example.ipynb' which loads a MIDI file and a text_file and prints labels like a file in 'csv' folder.


## 6. License <a name="license"></a>
CSD is created by the KAIST [Music and Audio Computing Lab](https://mac.kaist.ac.kr/) under Industrial Technology Innovation Program (No. 10080667, Development of conversational speech synthesis technology to express emotion and personality of robots through sound source diversification) supported support by the Ministry of Trade, Industry & Energy (MOTIE, Korea).

CSD is released under Creative Commons Atribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). It is provided primarily for research purposes and it is prohibited to be used for commercial purposes. When sharing your result based on CSD, any act that defames the original singer is strictly prohibited.

For more details, we refer to the following publication. We would highly appreciate if publications partly based on CSD quote the following publication:

> *Choi, S., Kim, W., Park, S., Yong, S., & Nam, J. (2020). [Children’s Song Dataset for Singing Voice Research](https://program.ismir2020.net/static/lbd/ISMIR2020-LBD-435-abstract.pdf). 21th International Society for Music Information Retrieval Conference (ISMIR)*.

## 7. Download <a name="download"></a>
[Download](https://zenodo.org/record/4785016#.YLYW6P0QtTa)