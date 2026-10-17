from sqlalchemy.orm import Session
from app.models.opportunity import Opportunity
from sqlalchemy import or_


class OpportunityRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Opportunity).offset(skip).limit(limit).all()

    def get_by_id(self, opportunity_id: str):
        return self.db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()

    def search(self, q: str | None = None, category: str | None = None, skip: int = 0, limit: int = 100):
        query = self.db.query(Opportunity)
        if q:
            query = query.filter(or_(
                Opportunity.title.ilike(f"%{q}%"),
                Opportunity.description.ilike(f"%{q}%"),
                Opportunity.provider.ilike(f"%{q}%"),
            ))
        if category:
            query = query.filter(Opportunity.category == category)
        return query.offset(skip).limit(limit).all()
