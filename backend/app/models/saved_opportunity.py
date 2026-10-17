from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
import uuid
from .base import Base, TimestampMixin


class SavedOpportunity(Base, TimestampMixin):
    __tablename__ = "saved_opportunities"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id: Mapped[str] = mapped_column(String(36))
    opportunity_id: Mapped[str] = mapped_column(String(36))
