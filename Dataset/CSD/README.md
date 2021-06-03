# CSD: Children's Song Dataset for Singing Voice Research
This repository contains detailed information about [Children's Song Dataset (CSD)](https://program.ismir2020.net/static/lbd/ISMIR2020-LBD-435-abstract.pdf). The official dataset is released via Zenodo in this [link](https://zenodo.org/record/4785016#.YLYW6P0QtTa).

CSD is open source dataset for singing voice research. This dataset contains 50 Korean and 50 English songs sung by one Korean female professional pop singer. Each song is recorded in two separate keys resulting in a total of 200 audio recordings. Each audio recording is paired with a MIDI transcription and lyrics annotations in both grapheme-level and phoneme-level.

1. [Dataset Structure](#dataset_structure)
2. [Vocal Recording](#vocal_recording)
3. [MIDI Transcription](#midi_transcription)
4. [Lyric Annotation](#lyric_annotation)
5. [Supplementary Code](#supplementary_code)
6. [License](#license)
7. [Download](#download)


## 1. Dataset Structure <a name="dataset_structure"></a>
```
(CSD)
├── english
│   ├── wav
│   ├── mid
│   ├── lyric
│   ├── txt
│   ├── csv
│   └── metadata.json
└── korean
    ├── wav
    ├── mid
    ├── lyric
    ├── txt
    ├── csv
    └── metadata.json
```

The entire data splits into Korean and English and each language splits into 'wav', 'mid', 'lyric', 'txt' and 'csv' folders. Each song has the identical filenames for each format. Each format represents following information. Additional information like original song name, tempo and time signature for each song can be found in 'metadata.json'.

- 'wav': Vocal recordings in 44.1kHz 16bit wav format
- 'mid': Score information in MIDI format
- 'lyric': Lyric information in grapheme-level
- 'txt': Lyric information in syllable and phoneme-level
- 'csv': Note onset and offset and syllable timing in comma-separated value (CSV) format

## 2. Vocal Recording <a name="vocal_recording"></a>
Children’s songs usually have various versions in different styles so one of them that suites for the singer is chosen. While recording vocals, the singer sang along with the background music tracks. She deliberately rendered the singing in a “plain” style refraining from expressive singing skills. The recording took place in a dedicated soundproof room. Singer recorded three to four takes for each song and the best parts are combined into a single audio track. Two identical songs with different keys are discriminated by character 'a' and 'b' at the end of a filename.

## 3. MIDI Transcription <a name="midi_transcription"></a>
The MIDI data consists of monophonic notes. Each note contains onset and offset times which were manually fine-tuned along with the corresponding syllable. MIDI notes do not include any expression data or control change messages because those parameters can be ambiguous to define for singing voice. Singing voice is an highly expressive sound and so it is hard to define precise onset timings and pitches. We assumed one syllable matches with one MIDI note and made the following criteria to represent various expressions in singing voice.

- A piano sound is used as a reference tone for the annotated MIDI to ensure the alignment with vocal.
- The rising pitch at the beginning of a note is included within a single note.
- The end of syllable is treated as the offset of a note.
- The breathing sound during short pauses is not treated as note onset or offset.
- Vibrations are treated as a single sustaining note.
- If a syllable is rendered with several different pitches, we annotated them as separate notes.

## 4. Lyric Annotation <a name="lyric_annotation"></a>
Text files represent pronunciation for the corresponding audio. Phonetic alignment is not included because the MIDI notes can be used for syllable timings. Text files in the 'lyric' folder contains raw text for corresponding audio and the 'txt' folder contains phoneme-level lyric representation. The phoneme-level lyric representation is annotated in a special text format. Phonemes in a syllable are tied with underbar('_') and syllables are separated with space(' ') as the example below.

In the 'lyric' folder
```
twinkle twinkle little star
```

In the 'text' folder
```
t_w_i_ng k_eo_l t_w_i_ng k_eo_l l_i t_eo_l s_t_a_r
```

Each phonemes are annotated based on the international phonetic alphabet (IPA) and romanized symbols are used to annotate IPA symbols. Following symbols are used for phoneme annotation.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-yla0{font-weight:bold;text-align:left;vertical-align:middle}
.tg .tg-nrix{text-align:center;vertical-align:middle}
</style>

### English

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" colspan="17"><span style="font-weight:bold">Consonant</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-yla0">Phoneme</td>
    <td class="tg-nrix">b</td>
    <td class="tg-nrix">d</td>
    <td class="tg-nrix">f</td>
    <td class="tg-nrix">g</td>
    <td class="tg-nrix">h</td>
    <td class="tg-nrix">j</td>
    <td class="tg-nrix">k</td>
    <td class="tg-nrix">l</td>
    <td class="tg-nrix">m</td>
    <td class="tg-nrix">n</td>
    <td class="tg-nrix">p</td>
    <td class="tg-nrix">r</td>
    <td class="tg-nrix">s</td>
    <td class="tg-nrix">t</td>
    <td class="tg-nrix">v</td>
    <td class="tg-nrix">w</td>
  </tr>
  <tr>
    <td class="tg-yla0">IPA</td>
    <td class="tg-nrix">b</td>
    <td class="tg-nrix">d</td>
    <td class="tg-nrix">f</td>
    <td class="tg-nrix">g</td>
    <td class="tg-nrix">h</td>
    <td class="tg-nrix">dʒ</td>
    <td class="tg-nrix">k</td>
    <td class="tg-nrix">l</td>
    <td class="tg-nrix">m</td>
    <td class="tg-nrix">n</td>
    <td class="tg-nrix">p</td>
    <td class="tg-nrix">r</td>
    <td class="tg-nrix">s</td>
    <td class="tg-nrix">t</td>
    <td class="tg-nrix">v</td>
    <td class="tg-nrix">w</td>
  </tr>
  <tr>
    <td class="tg-yla0">Phoneme</td>
    <td class="tg-nrix">z</td>
    <td class="tg-nrix">zh</td>
    <td class="tg-nrix">ch</td>
    <td class="tg-nrix">sh</td>
    <td class="tg-nrix">th</td>
    <td class="tg-nrix">dh</td>
    <td class="tg-nrix">ng</td>
    <td class="tg-nrix">y</td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
  </tr>
  <tr>
    <td class="tg-yla0">IPA</td>
    <td class="tg-nrix">z</td>
    <td class="tg-nrix">ʒ</td>
    <td class="tg-nrix">tʃ</td>
    <td class="tg-nrix">ʃ</td>
    <td class="tg-nrix">θ</td>
    <td class="tg-nrix">ð</td>
    <td class="tg-nrix">ŋ</td>
    <td class="tg-nrix">j</td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-baqh"></td>
  </tr>
</tbody>
</table>

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" colspan="17"><span style="font-weight:bold">Vowel</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-yla0">Phoneme</td>
    <td class="tg-nrix">ae</td>
    <td class="tg-nrix">ei</td>
    <td class="tg-nrix">e</td>
    <td class="tg-nrix">ii</td>
    <td class="tg-nrix">i</td>
    <td class="tg-nrix">ai</td>
    <td class="tg-nrix">a</td>
    <td class="tg-nrix">ou</td>
    <td class="tg-nrix">u</td>
    <td class="tg-nrix">ao</td>
    <td class="tg-nrix">uu</td>
    <td class="tg-nrix">oi</td>
    <td class="tg-nrix">au</td>
    <td class="tg-nrix">eo</td>
    <td class="tg-nrix">er</td>
    <td class="tg-nrix">oo</td>
  </tr>
  <tr>
    <td class="tg-yla0">IPA</td>
    <td class="tg-nrix">æ</td>
    <td class="tg-nrix">eɪ</td>
    <td class="tg-nrix">e</td>
    <td class="tg-nrix">i:</td>
    <td class="tg-nrix">ɪ</td>
    <td class="tg-nrix">aɪ</td>
    <td class="tg-nrix">ɒ</td>
    <td class="tg-nrix">oʊ</td>
    <td class="tg-nrix">ʊ</td>
    <td class="tg-nrix">ʌ</td>
    <td class="tg-nrix">u:</td>
    <td class="tg-nrix">ɔɪ</td>
    <td class="tg-nrix">aʊ</td>
    <td class="tg-nrix">ə</td>
    <td class="tg-nrix">ɜ:ʳ</td>
    <td class="tg-nrix">ɔ:</td>
  </tr>
</tbody>
</table>

### Korean

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" colspan="17"><span style="font-weight:bold">Consonant</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-yla0">Phoneme</td>
    <td class="tg-nrix">g</td>
    <td class="tg-nrix">kk</td>
    <td class="tg-nrix">n</td>
    <td class="tg-nrix">d</td>
    <td class="tg-nrix">tt</td>
    <td class="tg-nrix">r</td>
    <td class="tg-nrix">l</td>
    <td class="tg-nrix">m</td>
    <td class="tg-nrix">b</td>
    <td class="tg-nrix">pp</td>
    <td class="tg-nrix">s</td>
    <td class="tg-nrix">ss</td>
    <td class="tg-nrix">ng</td>
    <td class="tg-nrix">j</td>
    <td class="tg-nrix">jj</td>
    <td class="tg-nrix">ch</td>
  </tr>
  <tr>
    <td class="tg-yla0">IPA</td>
    <td class="tg-nrix">g</td>
    <td class="tg-nrix">k͈</td>
    <td class="tg-nrix">n</td>
    <td class="tg-nrix">d</td>
    <td class="tg-nrix">t͈</td>
    <td class="tg-nrix">ɾ</td>
    <td class="tg-nrix">l</td>
    <td class="tg-nrix">m</td>
    <td class="tg-nrix">b</td>
    <td class="tg-nrix">p͈</td>
    <td class="tg-nrix">s</td>
    <td class="tg-nrix">s͈</td>
    <td class="tg-nrix">ŋ</td>
    <td class="tg-nrix">ts</td>
    <td class="tg-nrix">ts͈</td>
    <td class="tg-nrix">tsʰ</td>
  </tr>
  <tr>
    <td class="tg-yla0">Phoneme</td>
    <td class="tg-nrix">k</td>
    <td class="tg-nrix">t</td>
    <td class="tg-nrix">p</td>
    <td class="tg-nrix">h</td>
    <td class="tg-nrix">y</td>
    <td class="tg-nrix">w</td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
  </tr>
  <tr>
    <td class="tg-yla0">IPA</td>
    <td class="tg-nrix">k</td>
    <td class="tg-nrix">t</td>
    <td class="tg-nrix">p</td>
    <td class="tg-nrix">h</td>
    <td class="tg-nrix">j</td>
    <td class="tg-nrix">w</td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-nrix"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
    <td class="tg-baqh"></td>
  </tr>
</tbody>
</table>

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow" colspan="10"><span style="font-weight:bold">Vowel</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-yla0">Phoneme</td>
    <td class="tg-nrix">a</td>
    <td class="tg-nrix">ae</td>
    <td class="tg-nrix">eo</td>
    <td class="tg-nrix">e</td>
    <td class="tg-nrix">o</td>
    <td class="tg-nrix">u</td>
    <td class="tg-nrix">eu</td>
    <td class="tg-nrix">ui</td>
    <td class="tg-nrix">i</td>
  </tr>
  <tr>
    <td class="tg-yla0">IPA</td>
    <td class="tg-nrix">a</td>
    <td class="tg-nrix">ɛ</td>
    <td class="tg-nrix">ʌ</td>
    <td class="tg-nrix">e</td>
    <td class="tg-nrix">o</td>
    <td class="tg-nrix">u</td>
    <td class="tg-nrix">ɯ</td>
    <td class="tg-nrix">ɰi</td>
    <td class="tg-nrix">i</td>
  </tr>
</tbody>
</table>

## 5. Supplementary Code <a name="supplementary_code"></a>
This repository also offers a dataset validation test code and a example code for loading a MIDI file with an accompanied text file. To test the dataset run the following command:
```
python test.py --data_path ./
```

If no problems are found in the dataset, you will get a result as below.
```
[Test Result]
- Test A: ✔ (200/200)
- Test B: ✔ (200/200)
- Test C: ✔ (200/200)
- Test D: ✔ (200/200)
[MIDI Summary]
Note Range: 54 ~ 76, Max Note Length: 0.450s
```
When loading MIDI or text file you can also refer to 'example.ipynb' which loads a MIDI file an accompanied text file and prints labels like a file in 'csv' folder using python.


## 6. License <a name="license"></a>
CSD is created by the KAIST [Music and Audio Computing Lab](https://mac.kaist.ac.kr/) under Industrial Technology Innovation Program (No. 10080667, Development of conversational speech synthesis technology to express emotion and personality of robots through sound source diversification) supported support by the Ministry of Trade, Industry & Energy (MOTIE, Korea).

CSD is released under Creative Commons Atribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). It is provided primarily for research purposes and it is prohibited to be used for commercial purposes. When sharing your result based on CSD, any act that defames the original singer is strictly prohibited.

For more details, we refer to the following publication. We would highly appreciate if publications partly based on CSD quote the following publication:

> *Choi, S., Kim, W., Park, S., Yong, S., & Nam, J. (2020). [Children’s Song Dataset for Singing Voice Research](https://program.ismir2020.net/static/lbd/ISMIR2020-LBD-435-abstract.pdf). 21th International Society for Music Information Retrieval Conference (ISMIR)*.

## 7. Download <a name="download"></a>
Download the dataset via Zenodo in this [link](https://zenodo.org/record/4785016#.YLYW6P0QtTa)