from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class OpportunityBase(BaseModel):
    title: str
    category: Optional[str] = None
    provider: Optional[str] = None
    description: Optional[str] = None
    education_requirements: Optional[str] = None
    eligibility_criteria: Optional[str] = None
    required_skills: Optional[List[str]] = None
    preferred_skills: Optional[List[str]] = None
    cost_or_stipend: Optional[str] = None
    location: Optional[str] = None
    mode: Optional[str] = None
    device_requirements: Optional[str] = None
    internet_requirements: Optional[str] = None
    official_source_url: Optional[str] = None
    application_url: Optional[str] = None
    application_deadline: Optional[date] = None
    is_individual_opportunity: bool = True
    verification_status: Optional[str] = None
    last_verified: Optional[str] = None


class OpportunityCreate(OpportunityBase):
    external_id: Optional[str] = None


class OpportunityRead(OpportunityBase):
    id: str
    external_id: Optional[str] = None

    class Config:
        from_attributes = True
