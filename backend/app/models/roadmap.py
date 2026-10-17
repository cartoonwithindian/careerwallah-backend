from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, ForeignKey
import uuid
from .base import Base, TimestampMixin


class Roadmap(Base, TimestampMixin):
    __tablename__ = "roadmaps"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id: Mapped[str] = mapped_column(String(36), ForeignKey("students.id"))
    career_direction: Mapped[str | None] = mapped_column(String(200), nullable=True)
    rationale: Mapped[str | None] = mapped_column(Text, nullable=True)
    milestones: Mapped[list | None] = mapped_column(JSON, nullable=True)
    recommended_skills: Mapped[list | None] = mapped_column(JSON, nullable=True)
    learning_resources: Mapped[list | None] = mapped_column(JSON, nullable=True)
    practical_tasks: Mapped[list | None] = mapped_column(JSON, nullable=True)
    progress_status: Mapped[str | None] = mapped_column(String(50), default="in_progress")

    student = relationship("Student", back_populates="roadmaps")
    steps = relationship("RoadmapStep", back_populates="roadmap")


class RoadmapStep(Base, TimestampMixin):
    __tablename__ = "roadmap_steps"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    roadmap_id: Mapped[str] = mapped_column(String(36), ForeignKey("roadmaps.id"))
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str | None] = mapped_column(String(50), default="not_started")
    order: Mapped[int] = mapped_column(default=0)

    roadmap = relationship("Roadmap", back_populates="steps")
