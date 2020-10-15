# CSD: Children's Song Dataset for Singing Voice Research
This repository contains Children's Song Dataset (CSD) which is open source dataset for singing voice research.
The dataset contains vocal recordings for 100 children's songs sung in Korean or English with MIDI transcriptions and lyric annotations.

**The dataset is still under development and we are plan to offer 50 Korean and 50 English songs as soon as possible.**

The dataset is composed of 50 Korean and 50 English songs sung by a Korean female professional pop singer. Each song is recorded in two separate keys, ranging from 2 to 5 semitones, resulting in a total of 200 audio recordings. We collected the children's songs to avoid the possible copyright issues in commercial pop music Each audio recording is paired with a MIDI transcription file and a lyrics annotation file.

# File Structure
The repository consists of following file structure. Entire data splits into Korean and English folders and each langauge folder contains 'wav', 'mid' and 'txt' folders.

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