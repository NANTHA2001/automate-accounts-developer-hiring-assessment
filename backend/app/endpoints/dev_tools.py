# app/api/endpoints/dev_tools.py
from datetime import datetime
from fastapi import APIRouter
from app.db import session, models
from app.core.ocr_utils import extract_text_from_pdf
import re

router = APIRouter()

@router.post("/reprocess-all")
def reprocess_all():
    db = session.SessionLocal()
    files = db.query(models.ReceiptFile).filter(models.ReceiptFile.is_valid == True).all()

    for f in files:
        text = extract_text_from_pdf(f.file_path)

        merchant = re.search(r"Welcome to (.+?) #", text)
        date_time = re.search(r"\d{2}/\d{2}/\d{2} \d{2}:\d{2}", text)
        total = re.search(r"Total\s+\$?([\d.]+)", text)
        if not total:
            total = re.search(r"USD\$?\s*([\d.]+)", text)

        # 🔍 Check if receipt already exists
        receipt = db.query(models.Receipt).filter_by(file_path=f.file_path).first()

        if receipt:
            # 🔁 Update existing
            receipt.merchant_name = merchant.group(1).strip() if merchant else "Unknown"
            receipt.purchased_at = date_time.group(0) if date_time else "Unknown"
            receipt.total_amount = float(total.group(1)) if total else 0.0
            receipt.updated_at = datetime.utcnow()
        else:
            # ➕ Add new
            receipt = models.Receipt(
                merchant_name=merchant.group(1).strip() if merchant else "Unknown",
                purchased_at=date_time.group(0) if date_time else "Unknown",
                total_amount=float(total.group(1)) if total else 0.0,
                file_path=f.file_path,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            db.add(receipt)

        f.is_processed = True
        f.updated_at = datetime.utcnow()

    db.commit()
    db.close()

    return {"message": "Reprocessing complete"}