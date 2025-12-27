
# AI@SOGANG project
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

>### 실행 방법

### 1) 의존성 설치 (requirements.txt 기준)
```bash
pip install -r requirements.txt

```

### 2) Streamlit 실행 

```code
streamlit run app.py
```


>### 파일 구조 및 역할

프로젝트의 파일 구조는 다음과 같습니다. 각 디렉토리와 파일의 역할은 아래에 설명되어 있습니다.

### root
- `app.py`: Streamlit 앱의 메인 파일. 음성 파일 업로드를 처리하고, 사용자 인터페이스를 제공합니다. Whisper 모델을 사용하여 ASR(자동 음성 인식)을 수행합니다.
- `README.md`: 프로젝트 설명, 실행 방법, 파일 구조 등을 담은 문서 파일입니다.
- `requirements.txt`: 프로젝트에 필요한 Python 패키지들의 목록입니다. 의존성을 설치할 때 사용됩니다.


### pages/
- `result.py`: Streamlit 멀티페이지 앱의 결과 페이지. 변환된 텍스트를 표시하고, 원본 오디오를 재생합니다. 

### src/
- `constants.py`: 앱에서 사용하는 상수들을 정의합니다. 예를 들어, 다양한 컨텍스트 프롬프트(일상 대화, 회의/업무 등)를 포함합니다.
- `db.py`: Supabase 데이터베이스와의 연동을 담당합니다. 음성 파일을 업로드하고, 메타데이터를 저장합니다.
- `model.py`: Whisper 모델을 로드하고, 음성 파일을 텍스트로 변환하는 기능을 제공합니다. model_action 함수를 통해 트랜스크립션을 수행합니다.
- `styles.py`: Streamlit 앱의 CSS 스타일을 정의합니다. UI의 외관을 꾸미기 위한 스타일 시트입니다.

