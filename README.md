				로봇의 감정 및 개성을 표현할 수 있는 대화형 음성합성 오픈소스 플랫폼
				===============================================================
Purpose
====
	본 음성합성 오픈소스는 산업통상자원부의 산업기술혁신사업으로부터 지원을 받아 한국과학기술원의 주관하에 (주)셀바스AI가 구축한 결과물이므로 연구 목적으로만 활용이 가능하고 상업을 목적으로 활용은 불가함. 
	(No. 10080667, 음원 다양화를 통하여 로봇의 감정 및 개성을 표현할 수 있는 대화음성합성 원천기술 개발)


Structure
====

```
├── CodeSet
│   ├── EmotionalSSMLParser : Emotinal SSML Parser
│   ├── SogangG2P           : Sogang G2P (Grapheme-to-Phoneme)
│   ├── Transformer-ParallelWaveGAN-based-Korean-TTS-master : Transformer-Parallel WaveGAN 기반 E2E 한국어 음성합성
│   └── realtimeMultiSpeakerMultiEmotionTTS : DNN 음성 합성기 (음색+감정)
└── Dataset
    ├── CSD             : Children's Song Dataset for Singing Voice Research
    └── SpeechCorpus    : 대화형 음성코퍼스 DB
        ├── Main
        ├── Personality
        └── Emotional  
```

License
====
1. 본 오픈소스는 산업통상자원부의 산업기술혁신사업으로부터 지원을 받아 한국과학기술원의 주관하에 (주)셀바스AI가 구축한 결과물이므로 연구 목적으로만 활용이 가능하고 상업을 목적으로 활용은 불가합니다
2. 본 오픈소스에 대하여 승인을 얻은 연구자가 아닌 제3자에게 열람하게 하거나 제공, 양도, 대여, 판매하지 아니한다
3. 본 오픈소스에 기반한 기술연구에 활용할 때에는 논문 등 결과물에 아래의 내용을 반드시 명기하여야 한다.
	- 국문 : 본 연구(혹은 프로젝트)는 산업통상자원부의 산업기술혁신사업으로부터 지원을 받아 수행된 연구(No. 10080667, 음원 다양화를 통하여 로봇의 감정 및 개성을 표현할 수 있는 대화음성합성 원천기술 개발)의 결과물인 오픈소스를 사용하였음.
	- 영문 : This study (or Project) used on open source as the result of research supported by the Ministry of Trade, Industry & Energy (MOTIE, Korea) under Industrial Technology Innovation Program (No. 10080667, Development of conversational speech synthesis technology to express emotion and personality of robots through sound source diversification).
4. 본 오픈소스에 기반하여 기술연구한 논문 등의 결과물에 대해 ㈜셀바스AI에 해당 정보를 제공하여야 한다.
5. 자료의 이용 및 그에 따른 연구로 인해 발생하는 모든 책임은 개인 및 해당 기관의 기관장에게 있다


Contacts
====
현 플랫폼 관련 이슈는 [이곳](https://github.com/emotiontts/emotiontts_open_db/issues)에 올려주세요.