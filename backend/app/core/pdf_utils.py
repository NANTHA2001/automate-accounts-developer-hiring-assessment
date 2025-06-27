# backend/app/core/pdf_utils.py
import magic

def is_pdf(file_path: str) -> bool:
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path) == "application/pdf"
