from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, JSON, Boolean, Date
import uuid
from .base import Base, TimestampMixin


class Opportunity(Base, TimestampMixin):
    __tablename__ = "opportunities"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    external_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    category: Mapped[str | None] = mapped_column(String(50), nullable=True)  # scholarship|job|internship|course|certification|portal
    provider: Mapped[str | None] = mapped_column(String(200), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    education_requirements: Mapped[str | None] = mapped_column(Text, nullable=True)
    eligibility_criteria: Mapped[str | None] = mapped_column(Text, nullable=True)
    required_skills: Mapped[list | None] = mapped_column(JSON, nullable=True)
    preferred_skills: Mapped[list | None] = mapped_column(JSON, nullable=True)
    cost_or_stipend: Mapped[str | None] = mapped_column(String(100), nullable=True)
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    mode: Mapped[str | None] = mapped_column(String(50), nullable=True)  # online|offline|hybrid
    device_requirements: Mapped[str | None] = mapped_column(Text, nullable=True)
    internet_requirements: Mapped[str | None] = mapped_column(Text, nullable=True)
    official_source_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    application_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    application_deadline: Mapped[Date | None] = mapped_column(Date, nullable=True)
    is_individual_opportunity: Mapped[bool] = mapped_column(Boolean, default=True)
    verification_status: Mapped[str | None] = mapped_column(String(50), nullable=True)  # unverified|verified|needs_verification
    last_verified: Mapped[str | None] = mapped_column(String(50), nullable=True)
