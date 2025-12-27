import streamlit as st
import tempfile
from src.model import get_whisper_model
from src.styles import GENERAL_CSS, DROPZONE_CSS,HIDE_SIDEBAR 
from src.constants import CONTEXTS



st.set_page_config(page_title="ASR", layout="wide")
st.title("🎙️ 음성 업로드 → 텍스트(ASR)")
st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)  # ✅ 추가
st.markdown(GENERAL_CSS, unsafe_allow_html=True)
ss = st.session_state

    
# ---- 세션 상태로 업로드 파일 관리 (리셋하려면 key를 바꿔야 함) ----
if "uploader_key" not in ss:
    ss.uploader_key = 0

def reset_uploader():
    ss.uploader_key += 1
    ss.uploaded_file = None

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Audio File")

    # 업로드된 파일을 session_state에 저장해두면 UI 전환이 매끄러움
    uploaded = ss.get("uploaded_file")
    st.markdown(DROPZONE_CSS, unsafe_allow_html=True) 
    if uploaded is None:
        # ✅ 업로드 전: 드롭존 보이기
        

        f = st.file_uploader(
            label="",
            type=["wav", "mp3", "m4a", "flac", "ogg"],
            key=f"uploader_{st.session_state.uploader_key}",
            label_visibility="collapsed",   
        )
        if f is not None:
            ss.uploaded_file = f
            st.rerun()

    else:
        
        #st.success("업로드 완료!")
        st.audio(uploaded)
        st.caption(f"파일명: {uploaded.name} / 크기: {uploaded.size/1024:.1f} KB")

        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("🔄 다른 파일 업로드", use_container_width=True):
                reset_uploader()
                st.rerun()
        with c2:
            st.download_button(
                "⬇️ 원본 파일 다운로드",
                data=uploaded.getvalue(),
                file_name=uploaded.name,
                mime=uploaded.type or "application/octet-stream",
                use_container_width=True,
            )

with col2:
    st.subheader("Context")
    context_name = st.selectbox("Select Context", list(CONTEXTS.keys()), index=0)
    ss.context_name = context_name
    ss.context_prompt = CONTEXTS[context_name]

    # 선택한 맥락 설명(나중에 TTS에 그대로 활용 가능)
    st.caption("선택된 맥락 설명")
    st.info(CONTEXTS[context_name])


st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)

l, m, r = st.columns([1, 1.2, 1])   # 가운데 칼럼을 살짝 넓게
with m:
    run = st.button(
        "🚀 변환 실행",
        type="primary",
        disabled=(ss.get("uploaded_file") is None),
        key="run_btn",
        use_container_width=True,   
    )
    
# if run:
#     st.switch_page("pages/result.py")
if "stt_text" not in ss:
    ss.stt_text = ""

if run:
    uploaded = ss.get("uploaded_file")
    if uploaded is None:
        st.warning("먼저 음성 파일을 업로드해줘.")
    else:
        # ✅ 결과 페이지에서 쓰기 위해 bytes로 저장(가장 안정적)
        ss.audio_name = uploaded.name
        ss.audio_type = uploaded.type
        ss.audio_bytes = uploaded.getvalue()

        ss.context_name = context_name
        ss.context_prompt = CONTEXTS[context_name]

        # ✅ result 페이지에서 변환하게 플래그만 켜기
        ss.need_transcribe = True
        ss.stt_text = ""  # 이전 결과 초기화(원하면 유지해도 됨)

        st.switch_page("pages/result.py")
