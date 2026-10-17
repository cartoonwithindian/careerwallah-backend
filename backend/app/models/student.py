from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, Boolean
import uuid
from .base import Base, TimestampMixin


class Student(Base, TimestampMixin):
    __tablename__ = "students"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    display_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    education_level: Mapped[str | None] = mapped_column(String(100), nullable=True)
    interests: Mapped[list | None] = mapped_column(JSON, nullable=True)
    skills: Mapped[list | None] = mapped_column(JSON, nullable=True)  # [{"skill": "python", "proficiency": 3}]
    career_goals: Mapped[list | None] = mapped_column(JSON, nullable=True)
    preferred_language: Mapped[str | None] = mapped_column(String(50), default="en")
    available_learning_hours: Mapped[float | None] = mapped_column(nullable=True)
    budget: Mapped[float | None] = mapped_column(nullable=True)
    device_access: Mapped[str | None] = mapped_column(String(50), nullable=True)
    internet_access: Mapped[str | None] = mapped_column(String(50), nullable=True)
    location: Mapped[str | None] = mapped_column(String(200), nullable=True)
    profile_visibility: Mapped[bool] = mapped_column(Boolean, default=True)

    roadmaps = relationship("Roadmap", back_populates="student")
    projects = relationship("Project", back_populates="author")
