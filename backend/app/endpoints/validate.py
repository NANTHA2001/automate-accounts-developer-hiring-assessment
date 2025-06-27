# backend/app/api/endpoints/validate.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.db import session, models
from app.core.pdf_utils import is_pdf

router = APIRouter()

class ValidateRequest(BaseModel):
    id: int

@router.post("")
def validate_pdf(req: ValidateRequest):
    db = session.SessionLocal()
    file_record = db.query(models.ReceiptFile).filter_by(id=req.id).first()

    if not file_record:
        db.close()
        return {"error": "File not found"}

    valid = is_pdf(file_record.file_path)
    file_record.is_valid = valid
    file_record.invalid_reason = None if valid else "Not a valid PDF"
    db.commit()
    db.refresh(file_record)
    db.close()

    return {"id": file_record.id, "is_valid": file_record.is_valid}
