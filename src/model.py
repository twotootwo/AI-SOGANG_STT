import streamlit as st
import whisper
import tempfile 
from src.db import upload_file

ss = st.session_state

@st.cache_resource(show_spinner=False)
def get_whisper_model(name: str):
    return whisper.load_model(name)


def model_action():
    
    context = ss.get("context_name")
    
    # 임시로 모델 호출한 부분
    suffix = ".wav"
    if ss.get("audio_name"):
        ext = ss.audio_name.split(".")[-1].lower()
        suffix = "." + ext
        
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(ss.audio_bytes)
        audio_path = tmp.name
        
    model = get_whisper_model("small")
    result = model.transcribe(audio_path, language="ko")
    result_text = result.get("text","").strip()
    
    # DB store
    upload_file(file_bytes=ss.audio_bytes, filename=ss.audio_name,transcription=result_text)
    
    # 텍스트 반환
    return result_text
    