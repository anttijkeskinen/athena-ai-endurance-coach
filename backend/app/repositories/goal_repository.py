from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.goal import Goal
from app.schemas.goal import GoalCreate, GoalUpdate


class GoalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        athlete_id: int,
        goal: GoalCreate,
    ) -> Goal:
        db_goal = Goal(
            athlete_id=athlete_id,
            **goal.model_dump(),
        )

        self.db.add(db_goal)
        self.db.commit()
        self.db.refresh(db_goal)

        return db_goal

    def get_all_for_athlete(
        self,
        athlete_id: int,
    ) -> list[Goal]:
        statement = (
            select(Goal)
            .where(Goal.athlete_id == athlete_id)
            .order_by(
                Goal.priority.asc(),
                Goal.target_date.asc().nulls_last(),
            )
        )

        return list(self.db.scalars(statement).all())

    def get_by_id(
        self,
        athlete_id: int,
        goal_id: int,
    ) -> Goal | None:
        statement = select(Goal).where(
            Goal.id == goal_id,
            Goal.athlete_id == athlete_id,
        )

        return self.db.scalar(statement)

    def update(
        self,
        goal: Goal,
        update_data: GoalUpdate,
    ) -> Goal:
        values = update_data.model_dump(exclude_unset=True)

        for field, value in values.items():
            setattr(goal, field, value)

        self.db.commit()
        self.db.refresh(goal)

        return goal

    def delete(self, goal: Goal) -> None:
        self.db.delete(goal)
        self.db.commit()