from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.database import Base


class Athlete(Base):
    __tablename__ = "athletes"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100))

    last_name: Mapped[str] = mapped_column(String(100))

    birth_year: Mapped[int] = mapped_column(Integer)

    sex: Mapped[str] = mapped_column(String(20))

    height_cm: Mapped[int] = mapped_column(Integer)

    country: Mapped[str] = mapped_column(
        String(10),
        default="FI"
    )

    timezone: Mapped[str] = mapped_column(
        String(50),
        default="Europe/Helsinki"
    )

    preferred_language: Mapped[str] = mapped_column(
        String(5),
        default="fi"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )