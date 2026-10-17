from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models import Roadmap, RoadmapStep

router = APIRouter(prefix="/roadmaps", tags=["roadmaps"])


@router.post("")
def create_roadmap(payload: Dict[str, Any], db: Session = Depends(get_db)):
    r = Roadmap(
        student_id=payload["student_id"],
        career_direction=payload.get("career_direction"),
        rationale=payload.get("rationale"),
        milestones=payload.get("milestones"),
        recommended_skills=payload.get("recommended_skills"),
        learning_resources=payload.get("learning_resources"),
        practical_tasks=payload.get("practical_tasks"),
    )
    db.add(r)
    db.commit()
    db.refresh(r)
    return r


@router.get("/students/{student_id}/roadmap")
def get_student_roadmap(student_id: str, db: Session = Depends(get_db)):
    r = db.query(Roadmap).filter(Roadmap.student_id == student_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Roadmap not found")
    return r


@router.patch("/{roadmap_id}")
def update_roadmap(roadmap_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    r = db.query(Roadmap).filter(Roadmap.id == roadmap_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Roadmap not found")
    for k, v in payload.items():
        if hasattr(r, k):
            setattr(r, k, v)
    db.commit()
    db.refresh(r)
    return r
