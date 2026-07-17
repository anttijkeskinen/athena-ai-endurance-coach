from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


DataSource = Literal[
    "manual",
    "garmin",
    "polar",
    "fit_import",
    "strava",
    "athena_estimate",
]


class PhysiologySnapshotCreate(BaseModel):
    measured_at: datetime

    weight_kg: Decimal | None = Field(
        default=None,
        gt=0,
        le=300,
    )
    body_fat_percent: Decimal | None = Field(
        default=None,
        ge=0,
        le=70,
    )

    ftp_watts: int | None = Field(
        default=None,
        gt=0,
        le=1000,
    )

    max_hr_bpm: int | None = Field(
        default=None,
        ge=80,
        le=240,
    )
    resting_hr_bpm: int | None = Field(
        default=None,
        ge=25,
        le=150,
    )
    resting_hr_min_bpm: int | None = Field(
        default=None,
        ge=25,
        le=150,
    )
    resting_hr_max_bpm: int | None = Field(
        default=None,
        ge=25,
        le=150,
    )

    running_threshold_hr_bpm: int | None = Field(
        default=None,
        ge=80,
        le=230,
    )
    cycling_threshold_hr_bpm: int | None = Field(
        default=None,
        ge=80,
        le=230,
    )

    vo2max_running: Decimal | None = Field(
        default=None,
        gt=0,
        le=100,
    )
    vo2max_cycling: Decimal | None = Field(
        default=None,
        gt=0,
        le=100,
    )

    hrv_ms: Decimal | None = Field(
        default=None,
        gt=0,
        le=500,
    )

    source: DataSource = "manual"
    notes: str | None = Field(default=None, max_length=500)

    @model_validator(mode="after")
    def validate_snapshot(self) -> "PhysiologySnapshotCreate":
        measured_values = [
            self.weight_kg,
            self.body_fat_percent,
            self.ftp_watts,
            self.max_hr_bpm,
            self.resting_hr_bpm,
            self.resting_hr_min_bpm,
            self.resting_hr_max_bpm,
            self.running_threshold_hr_bpm,
            self.cycling_threshold_hr_bpm,
            self.vo2max_running,
            self.vo2max_cycling,
            self.hrv_ms,
        ]

        if all(value is None for value in measured_values):
            raise ValueError(
                "At least one physiological measurement is required."
            )

        if (
            self.resting_hr_min_bpm is not None
            and self.resting_hr_max_bpm is not None
            and self.resting_hr_min_bpm > self.resting_hr_max_bpm
        ):
            raise ValueError(
                "resting_hr_min_bpm cannot exceed resting_hr_max_bpm."
            )

        return self


class PhysiologySnapshotResponse(PhysiologySnapshotCreate):
    id: int
    athlete_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)