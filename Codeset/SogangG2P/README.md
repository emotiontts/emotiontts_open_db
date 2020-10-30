# Sogang G2P (Grapheme-to-Phoneme)

## Requirements

* Python 3.5 이상
* TensorFlow 1.15

virtualenv를 이용하여 Python 가상환경을 만들기 위해서는 아래 명령을 입력합니다.

```bash
virtualenv -p python3 myenv
source myenv/bin/activate
```

아래 명령을 이용하여 필요한 패키지를 설치합니다.

```
pip install -r requirements.txt
```

## Running

모드는 총 2개가 있습니다. 기본값은 interactive로 설정되어 있습니다.

* interactive : 쉘에서 직접 타이핑 해서 결과를 확인가능
* decode : 파일을 입력으로 받아 변환 후 파일로 출력

### Interactive Mode
아래 명령을 이용하여 실행하실 수 있습니다.

```
python main.py --mode interactive
```

### Decode Mode
decode 모드는 입력과 출력 디렉토리명을 지정하면 디렉토리 내에 있는 파일을 읽어와 변환 후 파일로 출력합니다. 입력파일의 확장자는 `.txt`로 하셔야 합니다.

```
python main.py --mode decode --print_mode phoneme --in_path=INPUT_PATH --out_path=OUTPUT_PATH
```

아래 명령을 입력하면 input 디렉토리에 있는 파일을 읽어와 output 디렉토리에 .lbl 파일을 출력합니다.

```
python main.py --mode decode
```

### Options

print_mode에 대한 옵션은 아래와 같습니다.

| print_mode | Description        |
| ---------- | ------------------ |
| phoneme    | 음소 형태로 출력   |
| hangul     | 한글 발음으로 출력 |

## Copyright

본 프로젝트는 TensorFlow나 Numpy 등 공개소프트웨어를 이용하였으나, 데이터 처리 방법 및 모델 구현에 대한 저작권은 서강대학교 지능형 음성대화 인터페이스(ISDS) 연구실에 있습니다.