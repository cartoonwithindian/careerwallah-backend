from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models import Feedback

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("/projects/{project_id}/feedback")
def submit_feedback(project_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    f = Feedback(
        project_id=project_id,
        reviewer_id=payload.get("reviewer_id"),
        reviewer_role=payload.get("reviewer_role", "professional"),
        strengths=payload.get("strengths"),
        improvement_suggestions=payload.get("improvement_suggestions"),
        recommended_skills=payload.get("recommended_skills"),
        next_action=payload.get("next_action"),
        feedback_origin=payload.get("feedback_origin", "human"),
    )
    db.add(f)
    db.commit()
    db.refresh(f)
    return f


@router.get("/projects/{project_id}/feedback")
def get_project_feedback(project_id: str, db: Session = Depends(get_db)):
    return db.query(Feedback).filter(Feedback.project_id == project_id).all()


@router.post("/{feedback_id}/acknowledge")
def acknowledge_feedback(feedback_id: str, db: Session = Depends(get_db)):
    f = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not f:
        raise HTTPException(status_code=404, detail="Feedback not found")
    f.acknowledged = True
    db.commit()
    db.refresh(f)
    return f
