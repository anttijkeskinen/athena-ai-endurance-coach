from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.athlete_repository import AthleteRepository
from app.repositories.physiology_repository import PhysiologyRepository
from app.schemas.physiology import PhysiologySnapshotCreate


class PhysiologyService:
    def __init__(self, db: Session):
        self.athlete_repository = AthleteRepository(db)
        self.physiology_repository = PhysiologyRepository(db)

    def create_snapshot(
        self,
        athlete_id: int,
        snapshot: PhysiologySnapshotCreate,
    ):
        self._ensure_athlete_exists(athlete_id)

        return self.physiology_repository.create(
            athlete_id=athlete_id,
            snapshot=snapshot,
        )

    def get_history(self, athlete_id: int):
        self._ensure_athlete_exists(athlete_id)

        return self.physiology_repository.get_all_for_athlete(
            athlete_id
        )

    def get_latest(self, athlete_id: int):
        self._ensure_athlete_exists(athlete_id)

        snapshot = self.physiology_repository.get_latest_for_athlete(
            athlete_id
        )

        if snapshot is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No physiological measurements found",
            )

        return snapshot

    def _ensure_athlete_exists(self, athlete_id: int) -> None:
        athlete = self.athlete_repository.get_by_id(athlete_id)

        if athlete is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Athlete not found",
            )