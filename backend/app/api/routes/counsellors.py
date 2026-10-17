from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models import Counsellor, CounsellorBookingRequest

router = APIRouter(prefix="/counsellors", tags=["counsellors"])


@router.get("")
def list_counsellors(db: Session = Depends(get_db)):
    return db.query(Counsellor).all()


@router.get("/{counsellor_id}")
def get_counsellor(counsellor_id: str, db: Session = Depends(get_db)):
    return db.query(Counsellor).filter(Counsellor.id == counsellor_id).first()
