				로봇의 감정 및 개성을 표현할 수 있는 대화형 음성합성 오픈소스 플랫폼
				===============================================================
Purpose
====
	본 음성합성 오픈소스는 산업통상자원부의 산업기술혁신사업으로부터 지원을 받아 한국과학기술원의 주관하에 
    (주)셀바스AI가 구축한 결과물이므로 연구 목적으로만 활용이 가능하고 상업을 목적으로 활용은 불가함. 
	(No. 10080667, 음원 다양화를 통하여 로봇의 감정 및 개성을 표현할 수 있는 대화음성합성 원천기술 개발)


Structure
====

```
├── CodeSet
│   ├── EmotionalSSMLParser : Emotinal SSML Parser
│   ├── SogangG2P           : Sogang G2P (Grapheme-to-Phoneme)
│   ├── Transformer-ParallelWaveGAN-based-Korean-TTS-master 
│   │       : Transformer-Parallel WaveGAN 기반 E2E 한국어 음성합성
│   └── realtimeMultiSpeakerMultiEmotionTTS : DNN 음성 합성기 (음색+감정)
└── Dataset
    ├── CSD             : Children's Song Dataset for Singing Voice Research
    └── SpeechCorpus    : 대화형 음성코퍼스 DB
        ├── Main
        ├── Personality
        └── Emotional  
```

Contacts
====
현 플랫폼 관련 이슈는 [이곳](https://github.com/emotiontts/emotiontts_open_db/issues)에 올려주세요.