# styles.py - CSS 스타일 정의

GENERAL_CSS = """
<style>
/* 전체 앱 스타일링 */
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
}

.stApp {
    background: transparent;
}

/* 제목 스타일링 */
h1 {
    color: black !important;
    text-align: center;
    font-weight: 700;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    margin-bottom: 60px;
}

/* 섹션 카드 스타일링 */
div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    min-height: 300px; /* 균형을 위해 최소 높이 추가 */
}

/* 서브헤더 스타일링 */
h2 {
    color: #4a4a4a !important;
    font-weight: 600;
    margin-bottom: 50px;
    margin-top:100px;
}

/* 일반 버튼 스타일링 */
/* 변환하기 */
.stButton > button {
    background: linear-gradient(45deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
}

/* 선택박스 스타일링 */
.stSelectbox > div > div {
    background: rgba(255, 255, 255, 0.9) !important;
    border-radius: 10px !important;
    border: 1px solid #ddd !important;
}

/* 캡션 스타일링 */
.stCaption {
    color: #666 !important;
    font-style: italic;
}

/* 오디오 플레이어 스타일링 */
audio {
    width: 100%;
    border-radius: 10px;
}

div[data-testid="stButton"] button[kind="primary"] *,
div[data-testid="stButton"] button[data-testid="baseButton-primary"] *{
  height: 60px !important;
  border-radius: 26px !important;
  padding: 0 28px !important;
  font-size: 20px !important;
  font-weight: 700 !important;
  display: flex !important;          /* ✅ 가운데 정렬 */
  align-items: center !important;
  justify-content: center !important;
}
</style>
"""

DROPZONE_CSS = """
<style>
/* 드롭존 스타일링 */
div[data-testid="stFileUploader"]{
  position: relative;
  border: 2px dashed #bdbdbd;
  border-radius: 18px;
  padding: 28px;
  background: rgba(255, 255, 255, 0.9);
  min-height: 220px;
  overflow: hidden;
  box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
}

div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"]{
  border: 0 !important;
  background: transparent !important;
  padding: 0 !important;
}

div[data-testid="stFileUploader"] [data-testid="stFileUploaderDropzoneInstructions"],
div[data-testid="stFileUploader"] small,
div[data-testid="stFileUploader"] p{
  display: none !important;
}

/* 안내 텍스트 */
div[data-testid="stFileUploader"]::before{
  content: "🎵 여기로 음성 파일을 드래그 앤 드롭\\A또는 아래 버튼으로 파일 선택";
  white-space: pre;
  display: block;
  text-align: center;
  color: #666;
  font-size: 16px;
  line-height: 1.6;
  margin-top: 36px;
  position: relative;
  z-index: 1;
  font-weight: 500;
}

/* browse file */
div[data-testid="stFileUploader"] button{
  position: absolute !important;
  left: 50%;
  top: 80%;
  transform: translate(-50%, -50%);
  border-radius: 12px !important;
  padding: 10px 16px !important;
  font-size: 14px !important;
  cursor: pointer !important;
  z-index: 3;
  background: linear-gradient(45deg, #667eea, #764ba2) !important;
  color: white !important;
  border: none !important;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  transition: all 0.3s ease;
}

div[data-testid="stFileUploader"] button:hover{
  transform: translate(-50%, -50%) scale(1.05);
  box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

div[data-testid="stFileUploader"]:hover{
  border-color: #7d7d7d;
  background: rgba(255, 255, 255, 1);
  transform: scale(1.02);
  transition: all 0.3s ease;
}
</style>
"""
HIDE_SIDEBAR = """
<style>
/* 사이드바 영역 숨김 */
section[data-testid="stSidebar"] { display: none !important; }

/* 사이드바 때문에 생길 수 있는 좌측 여백 보정(버전별로 필요/불필요) */
div[data-testid="stAppViewContainer"] .main { margin-left: 0rem; }
</style>
"""

MIN_CSS = """
<style>
.stApp {
  background: linear-gradient(135deg, rgba(102,126,234,0.10) 0%, rgba(118,75,162,0.08) 100%);
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 800;
  background: rgba(102,126,234,0.12);
  border: 1px solid rgba(102,126,234,0.20);
  color: rgba(40,55,140,0.92);
  max-width: 100%;
}
.badge-text {
  display: inline-block;
  max-width: 900px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

textarea { border-radius: 12px !important; }
div[data-testid="stTextInput"] input { border-radius: 12px !important; }

div.stButton > button {
  width: 100%;
  border-radius: 12px;
  padding: 0.62rem 0.95rem;
  font-weight: 800;
  border: 1px solid rgba(0,0,0,0.08);
  box-shadow: 0 10px 22px rgba(0,0,0,0.06);
  transition: transform .08s ease, box-shadow .08s ease;
}
div.stButton > button:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 26px rgba(0,0,0,0.08);
}
</style>
"""
EXT_CSS =  """
            <div style="
              width:100%;
              text-align:center;
              padding:0.55rem 0.6rem;
              border-radius:12px;
              background: rgba(255,255,255,0.75);
              border: 1px solid rgba(0,0,0,0.08);
              font-weight:800;
              color: rgba(0,0,0,0.55);
              box-shadow: 0 10px 22px rgba(0,0,0,0.04);
            "> .txt </div>
            """
            
BADGE_CSS = """
            <span class="badge" title="선택된 Context가 없습니다.">
              ⚪ <span class="badge-text">Context 없음</span>
            </span>
            """