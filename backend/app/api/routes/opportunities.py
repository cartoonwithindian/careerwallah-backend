from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.session import get_db
from app.repositories.opportunity_repository import OpportunityRepository
from app.schemas.opportunity import OpportunityRead
from app.core.config import settings

router = APIRouter(prefix="/opportunities", tags=["opportunities"])


@router.get("", response_model=List[OpportunityRead])
def list_opportunities(
    q: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
):
    repo = OpportunityRepository(db)
    return repo.search(q=q, category=category, skip=skip, limit=limit)


@router.get("/{opportunity_id}", response_model=OpportunityRead)
def get_opportunity(opportunity_id: str, db: Session = Depends(get_db)):
    repo = OpportunityRepository(db)
    opp = repo.get_by_id(opportunity_id)
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return opp


@router.get("/categories", response_model=List[str])
def get_categories(db: Session = Depends(get_db)):
    repo = OpportunityRepository(db)
    results = db.query(Opportunity.category).distinct().all()
    return [r[0] for r in results if r[0]]


@router.get("/sources", response_model=List[str])
def get_sources(db: Session = Depends(get_db)):
    repo = OpportunityRepository(db)
    results = db.query(Opportunity.provider).distinct().all()
    return [r[0] for r in results if r[0]]
