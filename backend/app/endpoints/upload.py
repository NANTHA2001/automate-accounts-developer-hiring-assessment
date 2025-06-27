# backend/app/api/endpoints/upload.py

from fastapi import APIRouter, File, UploadFile, HTTPException
import os
from datetime import datetime
from app.db import session, models

router = APIRouter()
UPLOAD_DIR = "uploaded_receipts"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    contents = await file.read()
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save to disk
    with open(file_path, "wb") as f:
        f.write(contents)

    db = session.SessionLocal()

    # Check if the file already exists (based on filename)
    existing_file = db.query(models.ReceiptFile).filter_by(file_name=file.filename).first()

    if existing_file:
        existing_file.file_path = file_path
        existing_file.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(existing_file)
        db.close()
        return {"message": "File already exists, updated metadata", "id": existing_file.id}

    # Create new record
    receipt_file = models.ReceiptFile(
        file_name=file.filename,
        file_path=file_path,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        is_valid=False,
        is_processed=False,
    )
    db.add(receipt_file)
    db.commit()
    db.refresh(receipt_file)
    db.close()

    return {"message": "File uploaded", "id": receipt_file.id}
