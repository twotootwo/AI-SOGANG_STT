import re
import streamlit as st
from src.model import model_action
from src.styles import MIN_CSS, EXT_CSS,BADGE_CSS
st.set_page_config(page_title="Result", layout="wide")
ss = st.session_state

st.markdown(MIN_CSS, unsafe_allow_html=True)

def sanitize_filename(name: str) -> str:
    name = (name or "").strip()
    name = re.sub(r"\.txt$", "", name, flags=re.IGNORECASE)
    name = name.replace(" ", "_")
    name = re.sub(r"[^0-9A-Za-z가-힣_-]+", "", name)
    return name or "transcript"

def render_context_badge(context: str):
    context = (context or "").strip()
    if context:
        safe_title = context.replace('"', "'")
        st.markdown(
            f"""
            <span class="badge" title="{safe_title}">
              🧠 <span class="badge-text">{context}</span>
            </span>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            BADGE_CSS,
            unsafe_allow_html=True
        )

# Guard
if "audio_bytes" not in ss:
    st.warning("업로드된 파일이 없어요. 먼저 업로드 페이지에서 파일을 올려줘.")
    st.page_link("app.py", label="⬅️ 업로드 페이지로 돌아가기")
    st.stop()

# ✅ (필요 최소) 페이지 성격만 알려주는 텍스트 — 싫으면 이 줄도 지워도 됨
st.caption("변환된 텍스트를 확인하고, 필요하면 다시 변환할 수 있어요.")

# Top
st.markdown("**원본 오디오**")
st.audio(ss.audio_bytes)
render_context_badge(ss.get("context_prompt", ""))

st.divider()

# ✅ 버튼을 중앙에 모으기: 좌/우 여백 컬럼 크게
sp_l, b1, b2, sp_r = st.columns([2, 1, 1, 2], vertical_alignment="center")
with b1:
    if st.button("⬅️ 업로드로", use_container_width=True, key="btn_back"):
        st.switch_page("app.py")
with b2:
    if st.button("🔁 다시 변환", type="primary", use_container_width=True, key="btn_retry"):
        ss.need_transcribe = True

# 파일명 입력은 버튼 아래에 중앙 폭으로 두는 게 자연스러움
mid_l, mid, mid_r = st.columns([2, 1, 1])
with mid_l:
    st.markdown("**TXT 저장 파일명**")
    st.caption("여기에 입력한 이름으로 `.txt` 파일이 다운로드돼요. (확장자는 자동으로 붙습니다)")

    default_base = ss.get("audio_name") or ss.get("filename") or "transcript"

    name_col, ext_col = st.columns([4, 1], vertical_alignment="center")
    with name_col:
        st.text_input(
            "파일명",
            value=sanitize_filename(default_base),
            key="txt_filename",
            placeholder="예: meeting_lecture_01",
            label_visibility="collapsed",
        )
    with ext_col:
        # .txt를 시각적으로 고정 표시 (입력 불가)
        st.markdown(EXT_CSS,unsafe_allow_html=True)

st.divider()

# Transcribe
if ss.get("need_transcribe", False):
    with st.spinner("Whisper로 변환 중..."):
        ss.result_text = model_action()
    ss.need_transcribe = False
    

# Transcript (✅ 수정 불가)
st.subheader("Text Result")
st.text_area(
    "Transcript",
    value=ss.get("result_text", ""),
    height=420,
    key="ta_result",
    label_visibility="collapsed",
    disabled=True,  # ✅ 편집 불가
)

safe_base = sanitize_filename(ss.get("txt_filename", "transcript"))
st.download_button(
    "⬇️ TXT 다운로드",
    data=(ss.get("result_text", "") or ""),
    file_name=f"{safe_base}.txt",
    mime="text/plain",
    use_container_width=True
)
