from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, JSON, Boolean, ForeignKey
import uuid
from .base import Base, TimestampMixin


class Feedback(Base, TimestampMixin):
    __tablename__ = "feedback"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id"))
    reviewer_id: Mapped[str | None] = mapped_column(String(36))
    reviewer_role: Mapped[str | None] = mapped_column(String(50))
    strengths: Mapped[str | None] = mapped_column(Text)
    improvement_suggestions: Mapped[str | None] = mapped_column(Text)
    recommended_skills: Mapped[list | None] = mapped_column(JSON)
    next_action: Mapped[str | None] = mapped_column(Text)
    feedback_origin: Mapped[str | None] = mapped_column(String(50), default="human")
    acknowledged: Mapped[bool] = mapped_column(Boolean, default=False)

    project = relationship("Project", back_populates="feedback")
