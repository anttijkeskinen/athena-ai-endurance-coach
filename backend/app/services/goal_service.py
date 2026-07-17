from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.athlete_repository import AthleteRepository
from app.repositories.goal_repository import GoalRepository
from app.schemas.goal import GoalCreate, GoalUpdate


class GoalService:
    def __init__(self, db: Session):
        self.athlete_repository = AthleteRepository(db)
        self.goal_repository = GoalRepository(db)

    def create_goal(
        self,
        athlete_id: int,
        goal: GoalCreate,
    ):
        self._ensure_athlete_exists(athlete_id)

        return self.goal_repository.create(
            athlete_id=athlete_id,
            goal=goal,
        )

    def get_goals(self, athlete_id: int):
        self._ensure_athlete_exists(athlete_id)

        return self.goal_repository.get_all_for_athlete(
            athlete_id
        )

    def get_goal(
        self,
        athlete_id: int,
        goal_id: int,
    ):
        self._ensure_athlete_exists(athlete_id)

        goal = self.goal_repository.get_by_id(
            athlete_id=athlete_id,
            goal_id=goal_id,
        )

        if goal is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Goal not found",
            )

        return goal

    def update_goal(
        self,
        athlete_id: int,
        goal_id: int,
        update_data: GoalUpdate,
    ):
        goal = self.get_goal(
            athlete_id=athlete_id,
            goal_id=goal_id,
        )

        return self.goal_repository.update(
            goal=goal,
            update_data=update_data,
        )

    def delete_goal(
        self,
        athlete_id: int,
        goal_id: int,
    ) -> None:
        goal = self.get_goal(
            athlete_id=athlete_id,
            goal_id=goal_id,
        )

        self.goal_repository.delete(goal)

    def _ensure_athlete_exists(
        self,
        athlete_id: int,
    ) -> None:
        athlete = self.athlete_repository.get_by_id(
            athlete_id
        )

        if athlete is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Athlete not found",
            )