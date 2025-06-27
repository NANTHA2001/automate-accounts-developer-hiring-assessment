# backend/app/api/endpoints/process.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import session, models
from app.core.ocr_utils import extract_text_from_pdf
from datetime import datetime
import re

router = APIRouter()

class ProcessRequest(BaseModel):
    id: int

@router.post("")
def process_receipt(req: ProcessRequest):
    db = session.SessionLocal()
    file_record = db.query(models.ReceiptFile).filter_by(id=req.id).first()

    if not file_record or not file_record.is_valid:
        db.close()
        raise HTTPException(status_code=404, detail="Invalid or missing file")

    text = extract_text_from_pdf(file_record.file_path)

    merchant = re.search(r"Welcome to (.+?) #", text)
    date_time = re.search(r"\d{2}/\d{2}/\d{2} \d{2}:\d{2}", text)
    total = re.search(r"Total\s+\$?([\d.]+)", text)
    if not total:
        total = re.search(r"USD\$?\s*([\d.]+)", text)

    # 🔍 Check for existing receipt by file_path
    receipt = db.query(models.Receipt).filter_by(file_path=file_record.file_path).first()

    if receipt:
        # 🔁 Update it
        receipt.merchant_name = merchant.group(1).strip() if merchant else "Unknown"
        receipt.purchased_at = date_time.group(0) if date_time else "Unknown"
        receipt.total_amount = float(total.group(1)) if total else 0.0
        receipt.updated_at = datetime.utcnow()
    else:
        # ➕ Create new one
        receipt = models.Receipt(
            merchant_name=merchant.group(1).strip() if merchant else "Unknown",
            purchased_at=date_time.group(0) if date_time else "Unknown",
            total_amount=float(total.group(1)) if total else 0.0,
            file_path=file_record.file_path,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.add(receipt)

    file_record.is_processed = True
    file_record.updated_at = datetime.utcnow()

    db.commit()
    db.close()

    return {"message": "Receipt processed"}
