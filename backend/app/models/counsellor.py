from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, JSON, Boolean, ForeignKey, DateTime
import uuid
from .base import Base, TimestampMixin


class Counsellor(Base, TimestampMixin):
    __tablename__ = "counsellors"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100))
    title: Mapped[str | None] = mapped_column(String(200))
    organization: Mapped[str | None] = mapped_column(String(200))
    areas_of_expertise: Mapped[list | None] = mapped_column(JSON)
    bio: Mapped[str | None] = mapped_column(Text)
    service_fees: Mapped[str | None] = mapped_column(String(100))
    available: Mapped[bool] = mapped_column(Boolean, default=True)


class CounsellorBookingRequest(Base, TimestampMixin):
    __tablename__ = "counsellor_booking_requests"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id: Mapped[str] = mapped_column(String(36))
    counsellor_id: Mapped[str] = mapped_column(String(36))
    request_status: Mapped[str] = mapped_column(String(50), default="requested")
    preferred_time: Mapped[str | None] = mapped_column(String(200))
    notes: Mapped[str | None] = mapped_column(Text)
