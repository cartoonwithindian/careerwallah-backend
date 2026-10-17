from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, Boolean, ForeignKey
import uuid
from .base import Base, TimestampMixin


class Project(Base, TimestampMixin):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    author_id: Mapped[str] = mapped_column(String(36), ForeignKey("students.id"))
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text)
    problem_statement: Mapped[str | None] = mapped_column(Text)
    skills_used: Mapped[list | None] = mapped_column(JSON)
    learning_goal: Mapped[str | None] = mapped_column(Text)
    project_url: Mapped[str | None] = mapped_column(String(500))
    thumbnail_url: Mapped[str | None] = mapped_column(String(500))
    visibility: Mapped[str | None] = mapped_column(String(50), default="public")

    author = relationship("Student", back_populates="projects")
    feedback = relationship("Feedback", back_populates="project")
