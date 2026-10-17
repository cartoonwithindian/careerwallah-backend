import json
from pathlib import Path
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine
from app.models import Base, Opportunity


def load_dataset():
    data_path = Path(__file__).parent.parent / "backend" / "app" / "data" / "rural_opportunity_bridge_dataset.json"
    with open(data_path) as f:
        return json.load(f)


def seed():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        # Check if already seeded
        if db.query(Opportunity).count() > 0:
            print("Already seeded")
            return
        data = load_dataset()
        for item in data.get("opportunities", []):
            opp = Opportunity(
                external_id=item.get("external_id"),
                title=item["title"],
                category=item.get("category"),
                provider=item.get("provider"),
                description=item.get("description"),
                education_requirements=item.get("education_requirements"),
                eligibility_criteria=item.get("eligibility_criteria"),
                required_skills=item.get("required_skills") or [],
                preferred_skills=item.get("preferred_skills") or [],
                cost_or_stipend=item.get("cost_or_stipend"),
                location=item.get("location"),
                mode=item.get("mode"),
                device_requirements=item.get("device_requirements"),
                internet_requirements=item.get("internet_requirements"),
                official_source_url=item.get("official_source_url"),
                application_url=item.get("application_url"),
                application_deadline=item.get("application_deadline") if item.get("application_deadline") else None,
                is_individual_opportunity=item.get("is_individual_opportunity", True),
                verification_status=item.get("verification_status"),
                last_verified=item.get("last_verified"),
            )
            db.add(opp)
        db.commit()
        print("Seeded successfully")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
