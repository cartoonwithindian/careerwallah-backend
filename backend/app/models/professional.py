from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, Boolean, ForeignKey
import uuid
from .base import Base, TimestampMixin


class Professional(Base, TimestampMixin):
    __tablename__ = "professionals"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))
    title: Mapped[str | None] = mapped_column(String(200))
    organization: Mapped[str | None] = mapped_column(String(200))
    bio: Mapped[str | None] = mapped_column(Text)
    expertise_areas: Mapped[list | None] = mapped_column(JSON)
    skills: Mapped[list | None] = mapped_column(JSON)
    reviews_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    professional_skills = relationship("ProfessionalSkill", back_populates="professional")


class ProfessionalSkill(Base, TimestampMixin):
    __tablename__ = "professional_skills"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    professional_id: Mapped[str] = mapped_column(String(36), ForeignKey("professionals.id"))
    skill: Mapped[str] = mapped_column(String(100))
    proficiency: Mapped[int] = mapped_column(default=3)

    professional = relationship("Professional", back_populates="professional_skills")
