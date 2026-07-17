from fastapi import FastAPI

import app.models.athlete
import app.models.goal
import app.models.physiology

from app.api.athletes import router as athlete_router
from app.api.goals import router as goal_router
from app.api.physiology import router as physiology_router
from app.db.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ATHENA AI Endurance Coach",
    version="0.4.0",
    description="Personal endurance coaching and training platform",
)

app.include_router(athlete_router)
app.include_router(physiology_router)
app.include_router(goal_router)


@app.get("/")
def root():
    return {
        "application": "ATHENA",
        "version": "0.4.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }


@app.get("/version")
def version():
    return {
        "version": "0.4.0",
    }