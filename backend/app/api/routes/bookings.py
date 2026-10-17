from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models import CounsellorBookingRequest

router = APIRouter(prefix="/booking-requests", tags=["booking-requests"])


@router.post("")
def create_booking_request(payload: Dict[str, Any], db: Session = Depends(get_db)):
    b = CounsellorBookingRequest(
        student_id=payload["student_id"],
        counsellor_id=payload["counsellor_id"],
        preferred_time=payload.get("preferred_time"),
        notes=payload.get("notes"),
        request_status="requested",
    )
    db.add(b)
    db.commit()
    db.refresh(b)
    return b


@router.get("/students/{student_id}/booking-requests")
def get_student_bookings(student_id: str, db: Session = Depends(get_db)):
    return db.query(CounsellorBookingRequest).filter(CounsellorBookingRequest.student_id == student_id).all()


@router.patch("/{request_id}")
def update_booking(request_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    b = db.query(CounsellorBookingRequest).filter(CounsellorBookingRequest.id == request_id).first()
    if not b:
        raise HTTPException(status_code=404, detail="Booking request not found")
    if "request_status" in payload:
        b.request_status = payload["request_status"]
    db.commit()
    db.refresh(b)
    return b
