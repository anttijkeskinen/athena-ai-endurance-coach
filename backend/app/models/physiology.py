from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class PhysiologySnapshot(Base):
    __tablename__ = "physiology_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True)

    athlete_id: Mapped[int] = mapped_column(
        ForeignKey("athletes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    measured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    weight_kg: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    body_fat_percent: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    ftp_watts: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    max_hr_bpm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    resting_hr_bpm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    resting_hr_min_bpm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    resting_hr_max_bpm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    running_threshold_hr_bpm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    cycling_threshold_hr_bpm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    vo2max_running: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    vo2max_cycling: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    hrv_ms: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    source: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="manual",
    )

    notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )