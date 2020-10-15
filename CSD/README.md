# CSD: Children's Song Dataset for Singing Voice Research
This repository contains Children's Song Dataset (CSD) which is open source dataset for singing voice research.

**The dataset is still under development and we are plan to offer 50 Korean and 50 English songs and finish the entire dataset within a week.**

The dataset is composed of 50 Korean and 50 English songs sung by a Korean female professional pop singer. Each song is recorded in two separate keys, ranging from 2 to 5 semitones, resulting in a total of 200 audio recordings. Each audio recording is paired with a MIDI transcription file and a lyrics annotation file.

# Dataset Structure
The repository is constructed in the following structure. Entire data splits into Korean and English folders and each langauge folder splits into 'wav', 'mid' and 'txt' folders. The 'wav' folder contains audio files and the 'mid' folder contains MIDI files that represents score information for each audio. The 'txt' folder contains text files that represents pronunciation information. One song has the same file name for an audio, a MIDI, and a text.

```
(CSD)
├── Korean
│   ├── wav
│   ├── mid
│   └── txt
└── English
    ├── wav
    ├── mid
    ├── txt
    └── lyric
```

# MIDI Annotation
Singing voice is an highly expressive sound and so it is hard to define precise onset timings and pitches. We assumed one syllable matches with one MIDI note and made the following criteria to represent various expressions in singing voice.

- A piano sound is used as a reference tone for the annotated MIDI to ensure the alignment with vocal.
- The rising pitch at the beginning of a note is included within a single note.
- The end of syllable is treated as the offset of a note.
- The breathing sound during short pauses is not treated as note onset or offset.
- Vibrato is treated as a single sustaining note.
- If a syllable is rendered with several different pitches, we annotated them as separate notes.

# Note Annotation
Text files represent pronunciation information for the corresponding audio. We did not include phonetic alignment because the onset and offset of MIDI notes can be used for syllable timings. For Korean graphemes can also represent phonemes so each syllable in a text matches with one note in a MIDI file. When a syllable corresponds to multiple notes, it is replicated.


But for English graphemes do not matches with phonemes so the dataset offers both graphemes in the 'lyric' folder and phonemes in the 'txt' folder. A syllable in the 'txt' folder matches with a note in the 'mid' folder like Korean. Syllables are consist of phonemes that are tied with underbar('_') as the example below.

In the 'lyric' folder
```
Twinkle twinkle little star
```

In the 'text' folder
```
t_w_i_ng k_eo_l t_w_i_ng k_eo_l l_i t_eo_l s_t_a_r
```

Following symbols are used for phoneme annotation.

**Consonants**
| Phoneme | IPA |
|---------|-----|
| b       | b   |
| d       | d   |
| f       | f   |
| g       | g   |
| h       | h   |
| j       | dʒ  |
| k       | k   |
| l       | l   |
| m       | m   |
| n       | n   |
| p       | p   |
| r       | r   |
| s       | s   |
| t       | t   |
| v       | v   |
| w       | w   |
| z       | z   |
| zh      | ʒ   |
| ch      | tʃ  |
| sh      | ʃ   |
| th      | θ   |
| dh      | ð   |
| ng      | ŋ   |
| y       | j   |

**Vowels**
| Phoneme | IPA |
|---------|-----|
| ae      | æ   |
| ei      | eɪ  |
| e       | e   |
| ii      | i:  |
| i       | ɪ   |
| ai      | aɪ  |
| a       | ɒ   |
| ou      | oʊ  |
| u       | ʊ   |
| ao      | ʌ   |
| uu      | u:  |
| oi      | ɔɪ  |
| au      | aʊ  |
| eo      | ə   |
| er      | ɜ:ʳ |
| oo      | ɔ:  |

# Coming Soon
- 20 English songs, MIDI and text annoations are under confirmation
- Metadata for entire dataset that contains tempo and time signature

If you have any problem using the dataset or found prolbem in the dataset please leave issues about them.

# Reference
- [g2pE](https://github.com/Kyubyong/g2p)
- [KoG2P](https://github.com/scarletcho/KoG2P)
- [BEGANSing](https://github.com/SoonbeomChoi/BEGANSing)
