from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.physiology import (
    PhysiologySnapshotCreate,
    PhysiologySnapshotResponse,
)
from app.services.physiology_service import PhysiologyService


router = APIRouter(
    prefix="/athletes/{athlete_id}/physiology",
    tags=["Physiology"],
)


@router.post(
    "",
    response_model=PhysiologySnapshotResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_physiology_snapshot(
    athlete_id: int,
    snapshot: PhysiologySnapshotCreate,
    db: Session = Depends(get_db),
):
    service = PhysiologyService(db)

    return service.create_snapshot(
        athlete_id=athlete_id,
        snapshot=snapshot,
    )


@router.get(
    "",
    response_model=list[PhysiologySnapshotResponse],
)
def get_physiology_history(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    service = PhysiologyService(db)

    return service.get_history(athlete_id)


@router.get(
    "/latest",
    response_model=PhysiologySnapshotResponse,
)
def get_latest_physiology_snapshot(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    service = PhysiologyService(db)

    return service.get_latest(athlete_id)