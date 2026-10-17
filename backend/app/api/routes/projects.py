from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Dict, Any, List, Optional
from app.db.session import get_db
from app.models import Project

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("")
def create_project(payload: Dict[str, Any], db: Session = Depends(get_db)):
    p = Project(
        author_id=payload["author_id"],
        title=payload["title"],
        description=payload.get("description"),
        problem_statement=payload.get("problem_statement"),
        skills_used=payload.get("skills_used"),
        learning_goal=payload.get("learning_goal"),
        project_url=payload.get("project_url"),
        thumbnail_url=payload.get("thumbnail_url"),
        visibility=payload.get("visibility", "public"),
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return p


@router.get("")
def list_projects(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db)):
    return db.query(Project).offset(skip).limit(limit).all()


@router.get("/{project_id}")
def get_project(project_id: str, db: Session = Depends(get_db)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    return p


@router.patch("/{project_id}")
def update_project(project_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    for k, v in payload.items():
        if hasattr(p, k):
            setattr(p, k, v)
    db.commit()
    db.refresh(p)
    return p


@router.delete("/{project_id}")
def delete_project(project_id: str, db: Session = Depends(get_db)):
    p = db.query(Project).filter(Project.id == project_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(p)
    db.commit()
    return {"status": "deleted"}
