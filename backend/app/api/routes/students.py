from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models import Student

router = APIRouter(prefix="/students", tags=["students"])


@router.post("")
def create_student(payload: Dict[str, Any], db: Session = Depends(get_db)):
    s = Student(
        display_name=payload.get("display_name"),
        education_level=payload.get("education_level"),
        interests=payload.get("interests"),
        skills=payload.get("skills"),
        career_goals=payload.get("career_goals"),
        preferred_language=payload.get("preferred_language", "en"),
        available_learning_hours=payload.get("available_learning_hours"),
        budget=payload.get("budget"),
        device_access=payload.get("device_access"),
        internet_access=payload.get("internet_access"),
        location=payload.get("location"),
    )
    db.add(s)
    db.commit()
    db.refresh(s)
    return s


@router.get("/{student_id}")
def get_student(student_id: str, db: Session = Depends(get_db)):
    s = db.query(Student).filter(Student.id == student_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return s


@router.patch("/{student_id}")
def update_student(student_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    s = db.query(Student).filter(Student.id == student_id).first()
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    for k, v in payload.items():
        if hasattr(s, k):
            setattr(s, k, v)
    db.commit()
    db.refresh(s)
    return s


@router.get("/{student_id}/progress")
def get_progress(student_id: str):
    return {"student_id": student_id, "progress": {"completed": 0, "in_progress": 0}}
