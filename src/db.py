import streamlit as st
from supabase import create_client



url = st.secrets.get("SUPABASE_URL")
key = st.secrets.get("SUPABASE_KEY")

supabase = create_client(url, key)


def upload_file(file_bytes,filename,transcription :str):
    # A. audio bucket 에 파일 업로드
    bucket_name = "audio_bucket"
    file_path = f"uploads/{filename}"
    supabase.storage.from_(bucket_name).upload(path = file_path, file = file_bytes,file_options={"content_type": "audio/wav","upsert": "true"})
    # B. DB에 메타데이터 저장
    data = {
        "file_name": filename,
        "file_url": file_path,   
    }
    supabase.table("audio_records").insert(data).execute()