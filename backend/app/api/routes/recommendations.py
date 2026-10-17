from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.db.session import get_db
from app.repositories.opportunity_repository import OpportunityRepository
from app.schemas.opportunity import OpportunityRead
from app.services.recommendation_service import recommend

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.post("")
def get_recommendations(payload: Dict[str, Any], db: Session = Depends(get_db)):
    student = payload.get("student_profile", payload)
    repo = OpportunityRepository(db)
    opps = repo.search()
    recs = recommend(student, [o.__dict__ for o in opps])
    return {"recommendations": recs}


@router.get("/students/{student_id}")
def get_student_recommendations(student_id: str, db: Session = Depends(get_db)):
    # Demo mode
    student = {
        "id": student_id,
        "display_name": "Demo Student",
        "education_level": "Class 12",
        "interests": ["technology", "education"],
        "skills": [{"skill": "basic_computers", "proficiency": 3}],
    }
    repo = OpportunityRepository(db)
    opps = repo.search()
    recs = recommend(student, [o.__dict__ for o in opps])
    return {"student_id": student_id, "recommendations": recs}
