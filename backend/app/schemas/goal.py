from datetime import date, datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Sport = Literal[
    "cycling",
    "running",
    "skiing",
    "strength",
    "multisport",
]

GoalType = Literal[
    "event",
    "performance",
    "fitness",
    "consistency",
    "health",
]

GoalStatus = Literal[
    "planned",
    "active",
    "completed",
    "cancelled",
]


class GoalCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)

    sport: Sport
    goal_type: GoalType = "event"

    target_date: date | None = None

    priority: int = Field(
        default=3,
        ge=1,
        le=5,
        description="1 = highest priority, 5 = lowest priority",
    )

    status: GoalStatus = "planned"

    target_distance_km: Decimal | None = Field(
        default=None,
        gt=0,
        le=1000,
    )

    target_duration_minutes: int | None = Field(
        default=None,
        gt=0,
        le=10000,
    )

    target_result: str | None = Field(
        default=None,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
    )


class GoalUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
    )

    sport: Sport | None = None
    goal_type: GoalType | None = None
    target_date: date | None = None

    priority: int | None = Field(
        default=None,
        ge=1,
        le=5,
    )

    status: GoalStatus | None = None

    target_distance_km: Decimal | None = Field(
        default=None,
        gt=0,
        le=1000,
    )

    target_duration_minutes: int | None = Field(
        default=None,
        gt=0,
        le=10000,
    )

    target_result: str | None = Field(
        default=None,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
    )


class GoalResponse(GoalCreate):
    id: int
    athlete_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)