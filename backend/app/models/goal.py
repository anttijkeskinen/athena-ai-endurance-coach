from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Goal(Base):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(primary_key=True)

    athlete_id: Mapped[int] = mapped_column(
        ForeignKey("athletes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    sport: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        index=True,
    )

    goal_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="event",
    )

    target_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
        index=True,
    )

    priority: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=3,
    )

    status: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="planned",
        index=True,
    )

    target_distance_km: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    target_duration_minutes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    target_result: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )