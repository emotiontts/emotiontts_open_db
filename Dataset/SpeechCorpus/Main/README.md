
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
	o 발성목록 : 낭독체, 대화체
	o DB 구성 및 화자수 
		1) 기본화자 : 여성 1인
		2) 평균음성모델 개발용 : 여성 4인
		3) 화자적응 학습 및 테스트용 : 여성 2인, 남성 2인
	
	o 음성데이터 파일형식 : PCM WAVE signed 16bits, 22.05kHz, mono
	o 데이터량
		1) 기본화자(여성)
			: 6.500문장(낭독체 1,000문장, 대화체 5,500문장)
			: 음성데이터, 녹음 대본, 대본 철자전사
		2) 평균음성모델 개발용
			: 500문장 x 4명
			: 음성데이터, 녹음 대본, 대본 철자전사
		3) 화자적응 학습 및 테스트용
			: 100문장 x 4명
			: 음성데이터, 녹음 대본, 대본 철자전사

	o 디렉토리의 내용
		1) main	- 기본화자(여성)
			lmy/ - 기본화자 디렉토리	
				wav/ - 기본화자 음성 데이터
					: lmy00001.wav ~ lmy06500.wav
				script/ - 기본화자 녹음 대본(UTF-8)
					: lmy00001.txt ~ lmy06500.txt
				transcript/ - 기본화자 녹음 대본 철자전사(UTF-8)
					: lmy00001.txt ~ lmy06500.txt


		2) average_voice_model - 평균음성모델 개발용
			ava/ - 평균음성모델 A화자(여성) 디렉토리 
				wav/ - 평균음성모델 A화자 음성 데이터
					: ava00001.wav ~ ava00500.wav
				script/ - 평균음성모델 A화자 녹음 대본(UTF-8)
					: ava00001.txt ~ ava00500.txt
				transcript/ - 평균음성모델 A화자 녹음 대본 철자전사(UTF-8)
					: ava00001.txt ~ ava00500.txt

			avb/ - 평균음성모델 B화자(여성) 디렉토리 
				wav/ - 평균음성모델 B화자 음성 데이터
					: avb00001.wav ~ avb00500.wav
				script/ - 평균음성모델 B화자 녹음 대본(UTF-8)
					: avb00001.txt ~ avb00500.txt
				transcript/ - 평균음성모델 B화자 녹음 대본 철자전사(UTF-8)
					: avb00001.txt ~ avb00500.txt

			avc/ - 평균음성모델 C화자(여성) 디렉토리 
				wav/ - 평균음성모델 C화자 음성 데이터
					: avc00001.wav ~ avc00500.wav
				script/ - 평균음성모델 C화자 녹음 대본(UTF-8)
					: avc00001.txt ~ avc00500.txt
				transcript/ - 평균음성모델 C화자 녹음 대본 철자전사(UTF-8)
					: avc00001.txt ~ avc00500.txt

			avd/ - 평균음성모델 D화자(여성) 디렉토리 
				wav/ - 평균음성모델 D화자 음성 데이터
					: avd00001.wav ~ avd00500.wav
				script/ - 평균음성모델 D화자 녹음 대본(UTF-8)
					: avd00001.txt ~ avd00500.txt
				transcript/ - 평균음성모델 D화자 녹음 대본 철자전사(UTF-8)
					: avd00001.txt ~ avd00500.txt

		3) adaptive - 화자적응 학습 및 테스트용
			ada/ - 화자적응 A화자(여성) 디렉토리 
				wav/ - 화자적응 A화자 음성 데이터
					: ada00001.wav ~ ada00100.wav
				script/ - 화자적응 A화자 녹음 대본(UTF-8)
					: ada00001.txt ~ ada00100.txt
				transcript/ - 화자적응 A화자 녹음 대본 철자전사(UTF-8)
					: ada00001.txt ~ ada00100.txt

			adb/ - 화자적응 B화자(여성) 디렉토리 
				wav/ - 화자적응 B화자 음성 데이터
					: adb00001.wav ~ adb00100.wav
				script/ - 화자적응 B화자 녹음 대본(UTF-8)
					: adb00001.txt ~ adb00100.txt
				transcript/ - 화자적응 B화자 녹음 대본 철자전사(UTF-8)
					: adb00001.txt ~ adb00100.txt

			adc/ - 화자적응 C화자(남성) 디렉토리 
				wav/ - 화자적응 C화자 음성 데이터
					: adc00001.wav ~ adc00100.wav
				script/ - 화자적응 C화자 녹음 대본(UTF-8)
					: adc00001.txt ~ adc00100.txt
				transcript/ - 화자적응 C화자 녹음 대본 철자전사(UTF-8)
					: adc00001.txt ~ adc00100.txt

			add/ - 화자적응 D화자(남성) 디렉토리 
				wav/ - 화자적응 D화자 음성 데이터
					: add00001.wav ~ add00100.wav
				script/ - 화자적응 D화자 녹음 대본(UTF-8)
					: add00001.txt ~ add00100.txt
				transcript/ - 화자적응 D화자 녹음 대본 철자전사(UTF-8)
					: add00001.txt ~ add00100.txt


기타
====
    Contact	 :  서울시 금천구 가산디지털1로 19, 20층
                (주)셀바스에이아이
               	MAIL : TTS_Support@selvas.com


NEWS
====
	New in 2020.08.31
	 - 1st push

	New in 2019.12.13
	 - 1st push
