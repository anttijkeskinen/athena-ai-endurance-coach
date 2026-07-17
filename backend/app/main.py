from fastapi import FastAPI

from app.api.athletes import router as athlete_router
from app.db.database import Base, engine

# Tuo mallit, jotta SQLAlchemy rekisteröi ne
import app.models.athlete

# Luo taulut (myöhemmin tämä korvataan Alembic-migraatioilla)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ATHENA AI Endurance Coach",
    version="0.2.0",
    description="AI-powered endurance coaching platform",
)

# Rekisteröi API-reitit
app.include_router(athlete_router)


@app.get("/")
def root():
    return {
        "application": "ATHENA",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
    }