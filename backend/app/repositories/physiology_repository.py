from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.physiology import PhysiologySnapshot
from app.schemas.physiology import PhysiologySnapshotCreate


class PhysiologyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        athlete_id: int,
        snapshot: PhysiologySnapshotCreate,
    ) -> PhysiologySnapshot:
        db_snapshot = PhysiologySnapshot(
            athlete_id=athlete_id,
            **snapshot.model_dump(),
        )

        self.db.add(db_snapshot)
        self.db.commit()
        self.db.refresh(db_snapshot)

        return db_snapshot

    def get_all_for_athlete(
        self,
        athlete_id: int,
    ) -> list[PhysiologySnapshot]:
        statement = (
            select(PhysiologySnapshot)
            .where(PhysiologySnapshot.athlete_id == athlete_id)
            .order_by(PhysiologySnapshot.measured_at.desc())
        )

        return list(self.db.scalars(statement).all())

    def get_latest_for_athlete(
        self,
        athlete_id: int,
    ) -> PhysiologySnapshot | None:
        statement = (
            select(PhysiologySnapshot)
            .where(PhysiologySnapshot.athlete_id == athlete_id)
            .order_by(PhysiologySnapshot.measured_at.desc())
            .limit(1)
        )

        return self.db.scalar(statement)