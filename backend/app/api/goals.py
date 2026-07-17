from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.goal import (
    GoalCreate,
    GoalResponse,
    GoalUpdate,
)
from app.services.goal_service import GoalService


router = APIRouter(
    prefix="/athletes/{athlete_id}/goals",
    tags=["Goals"],
)


@router.post(
    "",
    response_model=GoalResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_goal(
    athlete_id: int,
    goal: GoalCreate,
    db: Session = Depends(get_db),
):
    service = GoalService(db)

    return service.create_goal(
        athlete_id=athlete_id,
        goal=goal,
    )


@router.get(
    "",
    response_model=list[GoalResponse],
)
def get_goals(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    service = GoalService(db)

    return service.get_goals(athlete_id)


@router.get(
    "/{goal_id}",
    response_model=GoalResponse,
)
def get_goal(
    athlete_id: int,
    goal_id: int,
    db: Session = Depends(get_db),
):
    service = GoalService(db)

    return service.get_goal(
        athlete_id=athlete_id,
        goal_id=goal_id,
    )


@router.patch(
    "/{goal_id}",
    response_model=GoalResponse,
)
def update_goal(
    athlete_id: int,
    goal_id: int,
    update_data: GoalUpdate,
    db: Session = Depends(get_db),
):
    service = GoalService(db)

    return service.update_goal(
        athlete_id=athlete_id,
        goal_id=goal_id,
        update_data=update_data,
    )


@router.delete(
    "/{goal_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_goal(
    athlete_id: int,
    goal_id: int,
    db: Session = Depends(get_db),
):
    service = GoalService(db)

    service.delete_goal(
        athlete_id=athlete_id,
        goal_id=goal_id,
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)