# Transformer-Parallel WaveGAN 기반 E2E 한국어 음성합성

## 목적
본 연구는 산업통상자원부의 산업기술혁신사업으로부터 지원을 받아 수행된 연구임 (No. 10080667, 음원 다양화를 통하여 로봇의 감정 및 개성을 표현할 수 있는 대화음성합성 원천기술 개발).

## 설명
오픈 소스를 바탕으로 Transformer-Parallel WaveGAN 기반 E2E 한국어 음성합성을 할 수 있는 코드 및 레시피

제공되는 기능:
- 입력 text를 mel-spectrogram으로 변환하는 Transformer 훈련 (__훈련 DB 필요__)
- 위의 훈련된 Transformer를 이용한 mel-spectrogram 합성
- Parallel WaveGAN을 이용한 waveform 합성 (__제공된 Parallel WaveGAN 모델 이용__)

특이사항:
- 입력 텍스트는 철자(char)와 음소(phn) 중 철자(char)로 처리
- Transformer에서 positional encoding을 더할 때 layer normalization을 활용

참고:
  - [ESPnet github](https://github.com/espnet/espnet)
  - [Parallel WaveGAN github](https://github.com/kan-bayashi/ParallelWaveGAN)
  - [Transformer TTS paper](https://arxiv.org/pdf/1809.08895.pdf)
  - [MultiSpeech paper](https://arxiv.org/pdf/2006.04664.pdf)
  - [Parallel WaveGAN paper](https://arxiv.org/pdf/1910.11480.pdf)     


## 설정
참고: 아래 (1) - (3)은 espnet v.0.6.0 기준 설치 방법으로, 최신 버전의 espnet 설치 방법과 다름.
### (1) Kaldi 설치
```
git clone https://github.com/kaldi-asr/kaldi
cd kaldi/tools
make -j <NUM-CPU>
sudo ./extras/install_mkl.sh
cd ../src
./configure
make -j clean depend; make -j <NUM-CPU>
cd ../..
```

이때 make -j \<NUM-CPU\> 도중 extras/check_dependencies.sh에서 오류 발생시 안내 문구 참고해서 해결해야 함.

### (2) CUDA_PATH 설정
```
CUDAROOT=/path/to/cuda

export PATH=$CUDAROOT/bin:$PATH
export LD_LIBRARY_PATH=$CUDAROOT/lib64:$LD_LIBRARY_PATH
export CFLAGS="-I$CUDAROOT/include $CFLAGS"
export CUDA_HOME=$CUDAROOT
export CUDA_PATH=$CUDAROOT
```

### (3) espnet 설치
```
git clone -q https://github.com/kan-bayashi/espnet.git -b fix_import
cd espnet && git fetch && git checkout -b v.0.7.0 4ad3247c850bb6696e4e2c3f7633c0153463dded
cd tools && make KALDI=/path/to/kaldi
make check_install
cd ..
```



### (4) 한국어 DB 폴더 생성
```
mkdir egs/<DB-NAME>
cp -r egs/ljspeech/tts1 egs/<DB-NAME>/tts1
```

### (5) 디렉토리 업데이트
파일들을 직접 위치에 맞게 추가하거나 덮어씌우기. 여기에서 egs/tmp는 위 (4)에서 만든 egs/\<DB-NAME\>에 해당함.  
(*주의: 기존 폴더와 파일들은 그대로 두되, 필요한 폴더 혹은 파일들만 추가 혹은 업데이트하는 방식이므로, 가장 바깥 폴더째로 덮어씌우면 안 되고 아래 명시된 것들만 추가하거나 덮어씌워야 함.*)

- 모델 관련
  - espnet/nets/pytorch_backend/transformer/embedding.py
  - espnet/nets/pytorch_backend/e2e_tts_transformer.py
  - utils/parallelwavegan 폴더
- 훈련 관련
  - egs/tmp/tts1/local 내의 파일들(clean_text.py, data_prep.sh)과 text 폴더
  - egs/tmp/tts1/conf/tuning/train_pytorch_transformer.v3.single.yaml
  - egs/tmp/tts1/run.sh
- 합성 관련
  - utils/espnet_inference.py
  - utils/text 폴더

## 훈련
```
cd egs/<DB-NAME>/tts1
./run.sh
```
- 미리 준비해야 할 것
  - jamo 라이브러리 설치: cd egs/\<DB-NAME\>/tts1 && . ./path.sh && pip install jamo
  - 훈련 DB: <DB-NAME> 폴더 안에 음원 파일들이 모두 담긴 wav 폴더와 스크립트 파일이 존재해야 함. 이때 wav 폴더 내의 음원 파일 목록과 스크립트 파일 내의 음원 파일 목록이 정확히 일치해야 함.
    - 음원 파일: wav 폴더 안에 전체 음원 파일들이 위치함. (확장자: .wav, sampling rate: 22050Hz)
    - 스크립트 파일: 모든 음원들에 대해 파일명 순서대로 정렬해서 파일 하나 당 다음과 같이 한 줄씩 작성  
      > 확장자_제외한_음원_파일명|텍스트     
    
    예: wav 폴더 안에 lmy01001.wav, lmy01002.wav 파일이 있을 때 스크립트 파일:  
      > lmy01001|아이들은 보통 다섯 개의 융합되지 않은 척추골로 되어 있어요.  
      > lmy01002|세계적으로 널리 알려진 아르헨티나의 민요 예술가예요.

- 바꿔줘야 할 것
  - run.sh 60번째 줄의 db_root
  - local/data_prep.sh 33번째 줄의 "lmy"와 39번째 줄의 "lmy_text.txt"를 각각 훈련에 사용할 DB의 화자명과 스크립트 파일명에 맞게 수정

- 바꿔줄 수 있는 것
  - GPU 메모리에 따라 config 파일에서 batch-bins 조절 가능
  - ./run.sh --gpu \<GPU\>로 사용하고자 하는 gpu 번호 지정 (default: 0, nccl이 설치된 경우 0,1과 같이 multi-gpu 가능)
  - ./run.sh --stage \<STAGE\>로 시작 stage 설정 가능  
  e.g. ./run.sh --gpu 1 --stage 3

## 합성
```
cd ../../../utils 혹은 cd /path/to/espnet/utils
conda activate /path/to/espnet/tools/venv
python espnet_inference.py
```
- 미리 준비해야 할 것
  - parallel_wavegan 라이브러리: /path/to/espnet/tools/venv/bin/pip install parallel_wavegan

- 바꿔줘야 할 것
  - espnet_inference.py 10번째 줄의 sys.path.append("/path/to/espnet")의 "/path/to/espnet"을 본인의 espnet 위치에 맞게 수정
  - 25번째 줄의 model_dir을 본인이 훈련시킨 transformer 모델의 위치에 맞게 수정
  - 50번째 줄과 52번째 줄의 pwgan_path, pwgan_conf를 알맞게 수정
  - 77번째 줄의 dict_path를 알맞게 수정

- 바꿔줄 수 있는 것
  - espnet_inference.py 89번째 줄의 input_texts 안의 입력 텍스트들을 원하는 대로 수정

## 오류 발생 시 해결책
- 훈련 중
  - /usr/bin/env: ‘python3\r’: No such file or directory → sudo apt install dos2unix; dos2unix local/clean_text.py
  - exp/생성된_실험_폴더명/train.log 참고

- 기타
  - ModuleNotFoundError: No module named ‘jamo’ → /path/to/espnet/tools/venv/bin/pip install jamo
  - parallel_wavegan 설치 중 AttributeError: type object ‘Callable’ has no attribute ‘_abc_registry’ → /path/to/espnet/tools/venv/bin/pip uninstall typing

## 저자
최연주 (wkadldppdy@kaist.ac.kr) @ KAIST SSSC LAB
  
