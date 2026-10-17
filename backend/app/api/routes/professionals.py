from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models import Professional

router = APIRouter(prefix="/professionals", tags=["professionals"])


@router.get("")
def list_professionals(db: Session = Depends(get_db)):
    return db.query(Professional).all()


@router.get("/{professional_id}")
def get_professional(professional_id: str, db: Session = Depends(get_db)):
    return db.query(Professional).filter(Professional.id == professional_id).first()


@router.get("/recommended-for-project/{project_id}")
def recommended_for_project(project_id: str):
    return []


@router.get("/{professional_id}/review-queue")
def review_queue(professional_id: str):
    return []


@router.get("/{professional_id}/reviews")
def reviews(professional_id: str):
    return []
