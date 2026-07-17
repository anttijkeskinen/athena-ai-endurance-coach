from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.athlete import AthleteCreate
from app.schemas.athlete import AthleteResponse

from app.services.athlete_service import AthleteService

router = APIRouter(
    prefix="/athletes",
    tags=["Athletes"],
)


@router.post(
    "",
    response_model=AthleteResponse,
)
def create_athlete(
    athlete: AthleteCreate,
    db: Session = Depends(get_db),
):

    service = AthleteService(db)

    return service.create(athlete)


@router.get(
    "",
    response_model=list[AthleteResponse],
)
def get_athletes(
    db: Session = Depends(get_db),
):

    service = AthleteService(db)

    return service.get_all()


@router.get(
    "/{athlete_id}",
    response_model=AthleteResponse,
)
def get_athlete(
    athlete_id: int,
    db: Session = Depends(get_db),
):

    service = AthleteService(db)

    athlete = service.get_by_id(athlete_id)

    if athlete is None:
        raise HTTPException(
            status_code=404,
            detail="Athlete not found",
        )

    return athlete