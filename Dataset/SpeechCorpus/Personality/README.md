
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
	o 제 작 일 : 2019년
	o 발성목록 : 낭독체, 대화체
	o DB 구성 및 화자수 
		1) 개성 표현 음성합성기 개발 고도화를 위한 음성 DB (16명)
			: 10대, 3명
			: 20~40대, 8명
			: 50대이상, 3명
			: 사투리, 2명		
	o 음성데이터 파일형식 : PCM WAVE signed 16bits, 22.05kHz, mono
	o 데이터량
		1) 개성 표현 음성합성기 개발 고도화를 위한 음성 DB
			: 9,347문장

	o 디렉토리의 내용
		pfa/	- 개성 표현 여성 A화자 디렉토리	
			wav/ - 개성 표현 여성 A화자 음성 데이터
				: pfa00001.wav ~ pfa00550.wav
			script/ - 개성 표현 여성 A화자 녹음 대본(UTF-8)
				: pfa00001.txt ~ pfa00550.txt
			transcript/ - 개성 표현 여성 A화자 녹음 대본 철자전사(UTF-8)
				: pfa00001.txt ~ pfa00550.txt

		pfb/		- 개성 표현 여성 B화자 디렉토리	
			wav/ - 개성 표현 여성 B화자 음성 데이터
				: pfb00001.wav ~ pfb00620.wav
			script/ - 개성 표현 여성 B화자 녹음 대본(UTF-8)
				: pfb00001.txt ~ pfb00620.txt
			transcript/ - 개성 표현 여성 B화자 녹음 대본 철자전사(UTF-8)
				: pfb00001.txt ~ pfb00620.txt

		pfc/		- 개성 표현 여성 C화자 디렉토리	
			wav/ - 개성 표현 여성 C화자 음성 데이터
				: pfc00001.wav ~ pfc00620.wav
			script/ - 개성 표현 여성 C화자 녹음 대본(UTF-8)
				: pfc00001.txt ~ pfc00620.txt
			transcript/ - 개성 표현 여성 C화자 녹음 대본 철자전사(UTF-8)
				: pfc00001.txt ~ pfc00620.txt				

		pfd/		- 개성 표현 여성 D화자 디렉토리	
			wav/ - 개성 표현 여성 D화자 음성 데이터
				: pfd00001.wav ~ pfd00620.wav
			script/ - 개성 표현 여성 D화자 녹음 대본(UTF-8)
				: pfd00001.txt ~ pfd00620.txt
			transcript/ - 개성 표현 여성 D화자 녹음 대본 철자전사(UTF-8)
				: pfd00001.txt ~ pfd00620.txt					

		pfi/		- 개성 표현 여성 I화자(10대) 디렉토리	
			wav/ - 개성 표현 여성 I화자 음성 데이터
				: pfi00001.wav ~ pfi00477.wav
			script/ - 개성 표현 여성 I화자 녹음 대본(UTF-8)
				: pfi00001.txt ~ pfi00477.txt
			transcript/ - 개성 표현 여성 I화자 녹음 대본 철자전사(UTF-8)
				: pfi00001.txt ~ pfi00477.txt				

		pfl/		- 개성 표현 여성 L화자(50대이상) 디렉토리	
			wav/ - 개성 표현 여성 L화자 음성 데이터
				: pfl00001.wav ~ pfl00700.wav
			script/ - 개성 표현 여성 L화자 녹음 대본(UTF-8)
				: pfl00001.txt ~ pfl00700.txt
			transcript/ - 개성 표현 여성 L화자 녹음 대본 철자전사(UTF-8)
				: pfl00001.txt ~ pfl00700.txt				

		pfm/		- 개성 표현 여성 M화자(50대이상) 디렉토리	
			wav/ - 개성 표현 여성 M화자 음성 데이터
				: pfm00001.wav ~ pfm00700.wav
			script/ - 개성 표현 여성 M화자 녹음 대본(UTF-8)
				: pfm00001.txt ~ pfm00700.txt
			transcript/ - 개성 표현 여성 M화자 녹음 대본 철자전사(UTF-8)
				: pfm00001.txt ~ pfm00700.txt				

		pfo/		- 개성 표현 여성 O화자(사투리) 디렉토리	
			wav/ - 개성 표현 여성 O화자 음성 데이터
				: pfo00001.wav ~ pfo00350.wav
			script/ - 개성 표현 여성 O화자 녹음 대본(UTF-8)
				: pfo00001.txt ~ pfo00350.txt
			transcript/ - 개성 표현 여성 O화자 녹음 대본 철자전사(UTF-8)
				: pfo00001.txt ~ pfo00350.txt

		pfp/		- 개성 표현 여성 P화자(사투리) 디렉토리	
			wav/ - 개성 표현 여성 P화자 음성 데이터
				: pfp00001.wav ~ pfp00350.wav
			script/ - 개성 표현 여성 P화자 녹음 대본(UTF-8)
				: pfp00001.txt ~ pfp00350.txt
			transcript/ - 개성 표현 여성 P화자 녹음 대본 철자전사(UTF-8)
				: pfp00001.txt ~ pfp00350.txt				

		pma/		- 개성 표현 남성 A화자 디렉토리	
			wav/ - 개성 표현 남성 A화자 음성 데이터
				: pma00001.wav ~ pma00630.wav
			script/ - 개성 표현 남성 A화자 녹음 대본(UTF-8)
				: pma00001.txt ~ pma00630.txt
			transcript/ - 개성 표현 남성 A화자 녹음 대본 철자전사(UTF-8)
				: pma00001.txt ~ pma00630.txt		

		pmb/		- 개성 표현 남성 B화자 디렉토리	
			wav/ - 개성 표현 남성 B화자 음성 데이터
				: pmb00001.wav ~ pmb00640.wav
			script/ - 개성 표현 남성 B화자 녹음 대본(UTF-8)
				: pmb00001.txt ~ pmb00640.txt
			transcript/ - 개성 표현 남성 B화자 녹음 대본 철자전사(UTF-8)
				: pmb00001.txt ~ pmb00640.txt

		pmc/		- 개성 표현 남성 C화자 디렉토리	
			wav/ - 개성 표현 남성 C화자 음성 데이터
				: pmc00001.wav ~ pmc00660.wav
			script/ - 개성 표현 남성 C화자 녹음 대본(UTF-8)
				: pmc00001.txt ~ pmc00660.txt
			transcript/ - 개성 표현 남성 C화자 녹음 대본 철자전사(UTF-8)
				: pmc00001.txt ~ pmc00660.txt

		pmd/		- 개성 표현 남성 D화자 디렉토리
			wav/ - 개성 표현 남성 D화자 음성 데이터
				: pmd00001.wav ~ pmd00660.wav
			script/ - 개성 표현 남성 D화자 녹음 대본(UTF-8)
				: pmd00001.txt ~ pmd00660.txt
			transcript/ - 개성 표현 남성 D화자 녹음 대본 철자전사(UTF-8)
				: pmd00001.txt ~ pmd00660.txt				

		pmi/		- 개성 표현 남성 I화자(10대) 디렉토리
			wav/ - 개성 표현 남성 I화자 음성 데이터
				: pmi00001.wav ~ pmi00550.wav
			script/ - 개성 표현 남성 I화자 녹음 대본(UTF-8)
				: pmi00001.txt ~ pmi00550.txt
			transcript/ - 개성 표현 남성 I화자 녹음 대본 철자전사(UTF-8)
				: pmi00001.txt ~ pmi00550.txt

		pmj/		- 개성 표현 남성 J화자(10대) 디렉토리	
			wav/ - 개성 표현 남성 J화자 음성 데이터
				: pmj00001.wav ~ pmj00620.wav
			script/ - 개성 표현 남성 J화자 녹음 대본(UTF-8)
				: pmj00001.txt ~ pmj00620.txt
			transcript/ - 개성 표현 남성 J화자 녹음 대본 철자전사(UTF-8)
				: pmj00001.txt ~ pmj00620.txt

		pml/		- 개성 표현 남성 L화자(50대이상) 디렉토리	
			wav/ - 개성 표현 남성 L화자 음성 데이터
				: pml00001.wav ~ pml00600.wav
			script/ - 개성 표현 남성 L화자 녹음 대본(UTF-8)
				: pml00001.txt ~ pml00600.txt
			transcript/ - 개성 표현 남성 L화자 녹음 대본 철자전사(UTF-8)
				: pml00001.txt ~ pml00600.txt				

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
