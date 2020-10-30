
				로봇의 감정 및 개성을 표현할 수 있는 대화형 음성코퍼스 DB 배포
				===========================================================

목적
====
	본 음성 DB는 산업통상자원부의 산업기술혁신사업으로부터 지원을 받아 한국과학기술원의 주관하에 
	(주)셀바스AI가 구축한 결과물이므로 	연구 목적으로만 활용이 가능하고 상업을 목적으로 활용은 불가함. 
	(No. 10080667, 음원 다양화를 통하여 로봇의 감정 및 개성을 표현할 수 있는 대화음성합성 원천기술 개발)

NOTICE
====
	본 Repository는 아래 기술된 전체 데이터의 5%만 공개된 것이며, 전체 데이터가 활용하고자 하는 기업 또는 
	개인은 아래의 링크된 신청서 작성하여 제출해야함. 
	이후 별도 별도의 심사를 거쳐 자료 제공 여부가 결정되며 미승인시 자료 제공이 거절될 수 있음.
	신청서 : http://naver.me/GaQSRZdm


내용
====
	o 제 작 일 : 2017 ~ 2018년
	o 발성목록 : 대화체
	o DB 구성 및 화자수 
		1) 감정 표현 기술 연구를 위한 연구용 DB (일반 대본) : 여성 2인, 남성 3인
			: 일반 대본에 감정을 부여하여 녹음.
			: 일반, 기쁨, 화남, 슬픔		
		2) 감정 표현 기술 연구를 위한 연구용 DB (감정 대본) : 여성 5인, 남성 5인
			: 감정 대본을 사용하여 녹음.
			: 일반, 기쁨, 화남, 슬픔		
	o 음성데이터 파일형식 : PCM WAVE signed 16bits, 22.05kHz, mono
	o 데이터량
		1) 감정 표현 기술 연구를 위한 연구용 DB (일반 대본)
			: 400문장(감정별 100문장) x 5명
			: 음성데이터, 녹음 대본, 대본 철자전사
		2) 감정 표현 기술 연구를 위한 연구용 DB (감정 대본)
			: 400문장(감정별 100문장) x 10명
			: 음성데이터, 녹음 대본, 대본 철자전사


	o 디렉토리의 내용
		1) plain-to-emotional : 감정 표현 기술 연구를 위한 연구용 DB (일반 대본)
			ema/ - 감정연구용 A화자(여성) 디렉토리 
				wav/ - 감정연구용 A화자 음성 데이터
					: ema00001.wav ~ ema00100.wav (일반)
					: ema00101.wav ~ ema00200.wav (기쁨)
					: ema00201.wav ~ ema00300.wav (화남)
					: ema00301.wav ~ ema00400.wav (슬픔)
				script/ - 감정연구용 A화자 녹음 대본(UTF-8)
					: ema00001.txt ~ ema00100.txt (일반)
					: ema00101.txt ~ ema00200.txt (기쁨)
					: ema00201.txt ~ ema00300.txt (화남)
					: ema00301.txt ~ ema00400.txt (슬픔)
				transcript/ - 감정연구용 A화자 녹음 대본 철자전사(UTF-8)
					: ema00001.txt ~ ema00100.txt (일반)
					: ema00101.txt ~ ema00200.txt (기쁨)
					: ema00201.txt ~ ema00300.txt (화남)
					: ema00301.txt ~ ema00400.txt (슬픔)

			emb/ - 감정연구용 B화자(여성) 디렉토리 
				wav/ - 감정연구용 B화자 음성 데이터
					: emb00001.wav ~ emb00100.wav (일반)
					: emb00101.wav ~ emb00200.wav (기쁨)
					: emb00201.wav ~ emb00300.wav (화남)
					: emb00301.wav ~ emb00400.wav (슬픔)
				script/ - 감정연구용 B화자 녹음 대본(UTF-8)
					: emb00001.txt ~ emb00100.txt (일반)
					: emb00101.txt ~ emb00200.txt (기쁨)
					: emb00201.txt ~ emb00300.txt (화남)
					: emb00301.txt ~ emb00400.txt (슬픔)
				transcript/ - 감정연구용 B화자 녹음 대본 철자전사(UTF-8)
					: emb00001.txt ~ emb00100.txt (일반)
					: emb00101.txt ~ emb00200.txt (기쁨)
					: emb00201.txt ~ emb00300.txt (화남)
					: emb00301.txt ~ emb00400.txt (슬픔)

			emf/ - 감정연구용 F화자(남성) 디렉토리 
				wav/ - 감정연구용 F화자 음성 데이터
					: emf00001.wav ~ emf00100.wav (일반)
					: emf00101.wav ~ emf00200.wav (기쁨)
					: emf00201.wav ~ emf00300.wav (화남)
					: emf00301.wav ~ emf00400.wav (슬픔)
				script/ - 감정연구용 F화자 녹음 대본(UTF-8)
					: emf00001.txt ~ emf00100.txt (일반)
					: emf00101.txt ~ emf00200.txt (기쁨)
					: emf00201.txt ~ emf00300.txt (화남)
					: emf00301.txt ~ emf00400.txt (슬픔)
				transcript/ - 감정연구용 F화자 녹음 대본 철자전사(UTF-8)
					: emf00001.txt ~ emf00100.txt (일반)
					: emf00101.txt ~ emf00200.txt (기쁨)
					: emf00201.txt ~ emf00300.txt (화남)
					: emf00301.txt ~ emf00400.txt (슬픔)

			emg/ - 감정연구용 G화자(남성) 디렉토리 
				wav/ - 감정연구용 G화자 음성 데이터
					: emg00001.wav ~ emg00100.wav (일반)
					: emg00101.wav ~ emg00200.wav (기쁨)
					: emg00201.wav ~ emg00300.wav (화남)
					: emg00301.wav ~ emg00400.wav (슬픔)
				script/ - 감정연구용 G화자 녹음 대본(UTF-8)
					: emg00001.txt ~ emg00100.txt (일반)
					: emg00101.txt ~ emg00200.txt (기쁨)
					: emg00201.txt ~ emg00300.txt (화남)
					: emg00301.txt ~ emg00400.txt (슬픔)
				transcript/ - 감정연구용 G화자 녹음 대본 철자전사(UTF-8)
					: emg00001.txt ~ emg00100.txt (일반)
					: emg00101.txt ~ emg00200.txt (기쁨)
					: emg00201.txt ~ emg00300.txt (화남)
					: emg00301.txt ~ emg00400.txt (슬픔)

			emh/ - 감정연구용 H화자(남성) 디렉토리 
				wav/ - 감정연구용 H화자 음성 데이터
					: emh00001.wav ~ emh00100.wav (일반)
					: emh00101.wav ~ emh00200.wav (기쁨)
					: emh00201.wav ~ emh00300.wav (화남)
					: emh00301.wav ~ emh00400.wav (슬픔)
				script/ - 감정연구용 H화자 녹음 대본(UTF-8)
					: emh00001.txt ~ emh00100.txt (일반)
					: emh00101.txt ~ emh00200.txt (기쁨)
					: emh00201.txt ~ emh00300.txt (화남)
					: emh00301.txt ~ emh00400.txt (슬픔)
				transcript/ - 감정연구용 H화자 녹음 대본 철자전사(UTF-8)
					: emh00001.txt ~ emh00100.txt (일반)
					: emh00101.txt ~ emh00200.txt (기쁨)
					: emh00201.txt ~ emh00300.txt (화남)
					: emh00301.txt ~ emh00400.txt (슬픔)


		2) emotional-to-emotional : 감정 표현 기술 연구를 위한 연구용 DB (감정 대본)
			nea/ - 감정연구용 A화자(여성) 디렉토리 
				wav/ - 감정연구용 A화자 음성 데이터
					: nea00001.wav ~ nea00100.wav (일반)
					: nea00101.wav ~ nea00200.wav (기쁨)
					: nea00201.wav ~ nea00300.wav (화남)
					: nea00301.wav ~ nea00400.wav (슬픔)
				script/ - 감정연구용 A화자 녹음 대본(UTF-8)
					: nea00001.txt ~ nea00100.txt (일반)
					: nea00101.txt ~ nea00200.txt (기쁨)
					: nea00201.txt ~ nea00300.txt (화남)
					: nea00301.txt ~ nea00400.txt (슬픔)
				transcript/ - 감정연구용 A화자 녹음 대본 철자전사(UTF-8)
					: nea00001.txt ~ nea00100.txt (일반)
					: nea00101.txt ~ nea00200.txt (기쁨)
					: nea00201.txt ~ nea00300.txt (화남)
					: nea00301.txt ~ nea00400.txt (슬픔)

			neb/ - 감정연구용 B화자(여성) 디렉토리 
				wav/ - 감정연구용 B화자 음성 데이터
					: neb00001.wav ~ neb00100.wav (일반)
					: neb00101.wav ~ neb00200.wav (기쁨)
					: neb00201.wav ~ neb00300.wav (화남)
					: neb00301.wav ~ neb00400.wav (슬픔)
				script/ - 감정연구용 B화자 녹음 대본(UTF-8)
					: neb00001.txt ~ neb00100.txt (일반)
					: neb00101.txt ~ neb00200.txt (기쁨)
					: neb00201.txt ~ neb00300.txt (화남)
					: neb00301.txt ~ neb00400.txt (슬픔)
				transcript/ - 감정연구용 B화자 녹음 대본 철자전사(UTF-8)
					: neb00001.txt ~ neb00100.txt (일반)
					: neb00101.txt ~ neb00200.txt (기쁨)
					: neb00201.txt ~ neb00300.txt (화남)
					: neb00301.txt ~ neb00400.txt (슬픔)

			nec/ - 감정연구용 C화자(여성) 디렉토리 
				wav/ - 감정연구용 C화자 음성 데이터
					: nec00001.wav ~ nec00100.wav (일반)
					: nec00101.wav ~ nec00200.wav (기쁨)
					: nec00201.wav ~ nec00300.wav (화남)
					: nec00301.wav ~ nec00400.wav (슬픔)
				script/ - 감정연구용 C화자 녹음 대본(UTF-8)
					: nec00001.txt ~ nec00100.txt (일반)
					: nec00101.txt ~ nec00200.txt (기쁨)
					: nec00201.txt ~ nec00300.txt (화남)
					: nec00301.txt ~ nec00400.txt (슬픔)
				transcript/ - 감정연구용 C화자 녹음 대본 철자전사(UTF-8)
					: nec00001.txt ~ nec00100.txt (일반)
					: nec00101.txt ~ nec00200.txt (기쁨)
					: nec00201.txt ~ nec00300.txt (화남)
					: nec00301.txt ~ nec00400.txt (슬픔)

			ned/ - 감정연구용 D화자(여성) 디렉토리 
				wav/ - 감정연구용 D화자 음성 데이터
					: ned00001.wav ~ ned00100.wav (일반)
					: ned00101.wav ~ ned00200.wav (기쁨)
					: ned00201.wav ~ ned00300.wav (화남)
					: ned00301.wav ~ ned00400.wav (슬픔)
				script/ - 감정연구용 D화자 녹음 대본(UTF-8)
					: ned00001.txt ~ ned00100.txt (일반)
					: ned00101.txt ~ ned00200.txt (기쁨)
					: ned00201.txt ~ ned00300.txt (화남)
					: ned00301.txt ~ ned00400.txt (슬픔)
				transcript/ - 감정연구용 D화자 녹음 대본 철자전사(UTF-8)
					: ned00001.txt ~ ned00100.txt (일반)
					: ned00101.txt ~ ned00200.txt (기쁨)
					: ned00201.txt ~ ned00300.txt (화남)
					: ned00301.txt ~ ned00400.txt (슬픔)

			nee/ - 감정연구용 E화자(여성) 디렉토리 
				wav/ - 감정연구용 E화자 음성 데이터
					: nee00001.wav ~ nee00100.wav (일반)
					: nee00101.wav ~ nee00200.wav (기쁨)
					: nee00201.wav ~ nee00300.wav (화남)
					: nee00301.wav ~ nee00400.wav (슬픔)
				script/ - 감정연구용 E화자 녹음 대본(UTF-8)
					: nee00001.txt ~ nee00100.txt (일반)
					: nee00101.txt ~ nee00200.txt (기쁨)
					: nee00201.txt ~ nee00300.txt (화남)
					: nee00301.txt ~ nee00400.txt (슬픔)
				transcript/ - 감정연구용 E화자 녹음 대본 철자전사(UTF-8)
					: nee00001.txt ~ nee00100.txt (일반)
					: nee00101.txt ~ nee00200.txt (기쁨)
					: nee00201.txt ~ nee00300.txt (화남)
					: nee00301.txt ~ nee00400.txt (슬픔)

			nek/ - 감정연구용 K화자(남성) 디렉토리 
				wav/ - 감정연구용 K화자 음성 데이터
					: nek00001.wav ~ nek00100.wav (일반)
					: nek00101.wav ~ nek00200.wav (기쁨)
					: nek00201.wav ~ nek00300.wav (화남)
					: nek00301.wav ~ nek00400.wav (슬픔)
				script/ - 감정연구용 K화자 녹음 대본(UTF-8)
					: nek00001.txt ~ nek00100.txt (일반)
					: nek00101.txt ~ nek00200.txt (기쁨)
					: nek00201.txt ~ nek00300.txt (화남)
					: nek00301.txt ~ nek00400.txt (슬픔)
				transcript/ - 감정연구용 K화자 녹음 대본 철자전사(UTF-8)
					: nek00001.txt ~ nek00100.txt (일반)
					: nek00101.txt ~ nek00200.txt (기쁨)
					: nek00201.txt ~ nek00300.txt (화남)
					: nek00301.txt ~ nek00400.txt (슬픔)

			nel/ - 감정연구용 L화자(남성) 디렉토리 
				wav/ - 감정연구용 L화자 음성 데이터
					: nel00001.wav ~ nel00100.wav (일반)
					: nel00101.wav ~ nel00200.wav (기쁨)
					: nel00201.wav ~ nel00300.wav (화남)
					: nel00301.wav ~ nel00400.wav (슬픔)
				script/ - 감정연구용 L화자 녹음 대본(UTF-8)
					: nel00001.txt ~ nel00100.txt (일반)
					: nel00101.txt ~ nel00200.txt (기쁨)
					: nel00201.txt ~ nel00300.txt (화남)
					: nel00301.txt ~ nel00400.txt (슬픔)
				transcript/ - 감정연구용 L화자 녹음 대본 철자전사(UTF-8)
					: nel00001.txt ~ nel00100.txt (일반)
					: nel00101.txt ~ nel00200.txt (기쁨)
					: nel00201.txt ~ nel00300.txt (화남)
					: nel00301.txt ~ nel00400.txt (슬픔)

			nem/ - 감정연구용 M화자(남성) 디렉토리 
				wav/ - 감정연구용 M화자 음성 데이터
					: nem00001.wav ~ nem00100.wav (일반)
					: nem00101.wav ~ nem00200.wav (기쁨)
					: nem00201.wav ~ nem00300.wav (화남)
					: nem00301.wav ~ nem00400.wav (슬픔)
				script/ - 감정연구용 M화자 녹음 대본(UTF-8)
					: nem00001.txt ~ nem00100.txt (일반)
					: nem00101.txt ~ nem00200.txt (기쁨)
					: nem00201.txt ~ nem00300.txt (화남)
					: nem00301.txt ~ nem00400.txt (슬픔)
				transcript/ - 감정연구용 M화자 녹음 대본 철자전사(UTF-8)
					: nem00001.txt ~ nem00100.txt (일반)
					: nem00101.txt ~ nem00200.txt (기쁨)
					: nem00201.txt ~ nem00300.txt (화남)
					: nem00301.txt ~ nem00400.txt (슬픔)

			nen/ - 감정연구용 N화자(남성) 디렉토리 
				wav/ - 감정연구용 N화자 음성 데이터
					: nen00001.wav ~ nen00100.wav (일반)
					: nen00101.wav ~ nen00200.wav (기쁨)
					: nen00201.wav ~ nen00300.wav (화남)
					: nen00301.wav ~ nen00400.wav (슬픔)
				script/ - 감정연구용 N화자 녹음 대본(UTF-8)
					: nen00001.txt ~ nen00100.txt (일반)
					: nen00101.txt ~ nen00200.txt (기쁨)
					: nen00201.txt ~ nen00300.txt (화남)
					: nen00301.txt ~ nen00400.txt (슬픔)
				transcript/ - 감정연구용 N화자 녹음 대본 철자전사(UTF-8)
					: nen00001.txt ~ nen00100.txt (일반)
					: nen00101.txt ~ nen00200.txt (기쁨)
					: nen00201.txt ~ nen00300.txt (화남)
					: nen00301.txt ~ nen00400.txt (슬픔)

			neo/ - 감정연구용 O화자(남성) 디렉토리 
				wav/ - 감정연구용 O화자 음성 데이터
					: neo00001.wav ~ neo00100.wav (일반)
					: neo00101.wav ~ neo00200.wav (기쁨)
					: neo00201.wav ~ neo00300.wav (화남)
					: neo00301.wav ~ neo00400.wav (슬픔)
				script/ - 감정연구용 O화자 녹음 대본(UTF-8)
					: neo00001.txt ~ neo00100.txt (일반)
					: neo00101.txt ~ neo00200.txt (기쁨)
					: neo00201.txt ~ neo00300.txt (화남)
					: neo00301.txt ~ neo00400.txt (슬픔)
				transcript/ - 감정연구용 O화자 녹음 대본 철자전사(UTF-8)
					: neo00001.txt ~ neo00100.txt (일반)
					: neo00101.txt ~ neo00200.txt (기쁨)
					: neo00201.txt ~ neo00300.txt (화남)
					: neo00301.txt ~ neo00400.txt (슬픔)


기타
====
    Contact	 :  서울시 금천구 가산디지털1로 19, 20층
                (주)셀바스에이아이
               	MAIL : TTS_Support@selvas.com


NEWS
====
	New in 2020.08.31
	 - 2nd push

	New in 2019.12.13
	 - 1st push
