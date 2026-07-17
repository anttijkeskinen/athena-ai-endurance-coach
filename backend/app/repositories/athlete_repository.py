from sqlalchemy.orm import Session

from app.models.athlete import Athlete
from app.schemas.athlete import AthleteCreate


class AthleteRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, athlete: AthleteCreate) -> Athlete:

        db_athlete = Athlete(
            first_name=athlete.first_name,
            last_name=athlete.last_name,
            birth_year=athlete.birth_year,
            sex=athlete.sex,
            height_cm=athlete.height_cm,
            country=athlete.country,
            timezone=athlete.timezone,
            preferred_language=athlete.preferred_language,
        )

        self.db.add(db_athlete)
        self.db.commit()
        self.db.refresh(db_athlete)

        return db_athlete

    def get_all(self):

        return self.db.query(Athlete).all()

    def get_by_id(self, athlete_id: int):

        return (
            self.db.query(Athlete)
            .filter(Athlete.id == athlete_id)
            .first()
        )