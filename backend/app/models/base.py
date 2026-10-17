from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, func


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
