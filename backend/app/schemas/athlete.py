from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class AthleteCreate(BaseModel):
    first_name: str
    last_name: str
    birth_year: int
    sex: str
    height_cm: int

    country: str = "FI"
    timezone: str = "Europe/Helsinki"
    preferred_language: str = "fi"


class AthleteResponse(BaseModel):
    id: int

    first_name: str
    last_name: str

    birth_year: int
    sex: str
    height_cm: int

    country: str
    timezone: str
    preferred_language: str

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )