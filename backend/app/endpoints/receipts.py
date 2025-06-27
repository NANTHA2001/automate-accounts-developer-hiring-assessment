# backend/app/api/endpoints/receipts.py

from fastapi import APIRouter
from app.db import session, models

router = APIRouter()

@router.get("")
def list_receipts():
    db = session.SessionLocal()
    receipts = db.query(models.Receipt).all()
    db.close()
    return receipts

@router.get("/{receipt_id}")
def get_receipt(receipt_id: int):
    db = session.SessionLocal()
    receipt = db.query(models.Receipt).filter_by(id=receipt_id).first()
    db.close()
    if receipt:
        return receipt
    return {"error": "Not found"}
