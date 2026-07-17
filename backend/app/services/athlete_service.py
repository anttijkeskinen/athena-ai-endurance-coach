from sqlalchemy.orm import Session

from app.repositories.athlete_repository import AthleteRepository
from app.schemas.athlete import AthleteCreate


class AthleteService:

    def __init__(self, db: Session):
        self.repository = AthleteRepository(db)

    def create(self, athlete: AthleteCreate):
        return self.repository.create(athlete)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, athlete_id: int):
        return self.repository.get_by_id(athlete_id)