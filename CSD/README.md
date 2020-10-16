# CSD: Children's Song Dataset for Singing Voice Research
This repository contains [Children's Song Dataset (CSD)](https://soonbeomchoi.github.io/CSD-Blog/) which is open source dataset for singing voice research.

**The dataset is still under development and we are plan to offer 50 Korean and 50 English songs and finish the entire dataset within a week.**

The dataset is composed of 50 Korean and 50 English songs sung by one Korean female professional pop singer. Each song is recorded in two separate keys resulting in a total of 200 audio recordings. Each audio recording is paired with a MIDI transcription file and a lyrics annotation file.

You can also access the dataset through [this link](https://drive.google.com/drive/folders/12sN_9XpdBq5GbN9S9H3vmW7-6rPWiQZs?usp=sharing), the dataset version of this repository might be behind the latest version.

# Dataset Structure
The repository is constructed in the following structure. Entire data splits into Korean and English and each langauge splits into 'wav', 'mid' and 'txt' folders. The 'wav' folder contains audio files and the 'mid' folder contains MIDI files that represent score information for each audio. The 'txt' folder contains text files that represents pronunciation information. One song has the same name for an audio, a MIDI, and a text.

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

# MIDI Transcription
Singing voice is an highly expressive sound and so it is hard to define precise onset timings and pitches. We assumed one syllable matches with one MIDI note and made the following criteria to represent various expressions in singing voice.

- A piano sound is used as a reference tone for the annotated MIDI to ensure the alignment with vocal.
- The rising pitch at the beginning of a note is included within a single note.
- The end of syllable is treated as the offset of a note.
- The breathing sound during short pauses is not treated as note onset or offset.
- Vibrato is treated as a single sustaining note.
- If a syllable is rendered with several different pitches, we annotated them as separate notes.

# Lyric Annotation
Text files represent pronunciation for the corresponding audio. We did not include phonetic alignment because the MIDI notes can be used for syllable timings. For Korean, graphemes match with phonemes so a syllable in a text matches with one note in a MIDI file. When a syllable corresponds to multiple notes, it is replicated.


But for English, graphemes do not matches with phonemes so the dataset offers both graphemes in the 'lyric' folder and phonemes in the 'txt' folder. A syllable in the 'txt' folder matches with a note in the 'mid' folder like Korean. For each word, phonemes are tied with underbar('_') and each syllable has one vowel as the example below.

In the 'lyric' folder
```
twinkle twinkle little star
```

In the 'text' folder
```
t_w_i_ng_k_eo_l t_w_i_ng_k_eo_l l_i_t_eo_l s_t_a_r
```

Following symbols are used for phoneme annotation.

| Phoneme | IPA | Phoneme | IPA |
|---------|-----|---------|-----|
| b       | b   | ae      | æ   |
| d       | d   | ei      | eɪ  |
| f       | f   | e       | e   |
| g       | g   | ii      | i:  |
| h       | h   | i       | ɪ   |
| j       | dʒ  | ai      | aɪ  |
| k       | k   | a       | ɒ   |
| l       | l   | ou      | oʊ  |
| m       | m   | u       | ʊ   |
| n       | n   | ao      | ʌ   |
| p       | p   | uu      | u:  |
| r       | r   | oi      | ɔɪ  |
| s       | s   | au      | aʊ  |
| t       | t   | eo      | ə   |
| v       | v   | er      | ɜ:ʳ |
| w       | w   | oo      | ɔ:  |
| z       | z   |
| zh      | ʒ   |
| ch      | tʃ  |
| sh      | ʃ   |
| th      | θ   |
| dh      | ð   |
| ng      | ŋ   |
| y       | j   |


# Coming Soon
- 20 English songs, MIDI and text annoations are under confirmation
- Metadata for entire dataset that contains tempo and time signature

If you have any problem using the dataset or found prolbem in the dataset please leave issues about them.

# Reference
- [g2pE](https://github.com/Kyubyong/g2p)
- [KoG2P](https://github.com/scarletcho/KoG2P)
- [BEGANSing](https://github.com/SoonbeomChoi/BEGANSing)