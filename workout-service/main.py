# workout-service/main.py
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db
import db_models
from models import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from service import WorkoutService
import data_service

# Create DB tables automatically
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Workout Service API",
    description="Microservice for managing gym workout plans - Developed by Pabasara",
    version="1.0.0"
)

workout_service = WorkoutService()


# ── Seed data on startup ──────────────────────────────────
@app.on_event("startup")
def startup_event():
    db = next(get_db())
    data_service.seed_data(db)


# ── Health ────────────────────────────────────────────────

@app.get("/", tags=["Health"])
def root():
    return {
        "service": "Workout Service",
        "status": "running",
        "developer": "Pabasara",
        "port": 8003
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "service": "workout-service"}


# ── Workout Endpoints ─────────────────────────────────────

@app.get(
    "/api/workouts",
    response_model=List[WorkoutResponse],
    tags=["Workouts"],
    summary="Get all workout plans"
)
def get_all_workouts(db: Session = Depends(get_db)):
    """Get all workout plans"""
    return workout_service.get_all(db)


@app.get(
    "/api/workouts/{workout_id}",
    response_model=WorkoutResponse,
    tags=["Workouts"],
    summary="Get a workout by ID"
)
def get_workout(workout_id: int, db: Session = Depends(get_db)):
    """Get a workout plan by ID"""
    workout = workout_service.get_by_id(db, workout_id)
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


@app.post(
    "/api/workouts",
    response_model=WorkoutResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Workouts"],
    summary="Create a new workout plan"
)
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    """Create a new workout plan"""
    return workout_service.create(db, workout)


@app.put(
    "/api/workouts/{workout_id}",
    response_model=WorkoutResponse,
    tags=["Workouts"],
    summary="Update an existing workout plan"
)
def update_workout(workout_id: int, workout: WorkoutUpdate, db: Session = Depends(get_db)):
    """Update a workout plan"""
    updated = workout_service.update(db, workout_id, workout)
    if not updated:
        raise HTTPException(status_code=404, detail="Workout not found")
    return updated


@app.delete(
    "/api/workouts/{workout_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Workouts"],
    summary="Delete a workout plan"
)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    """Delete a workout plan"""
    success = workout_service.delete(db, workout_id)
    if not success:
        raise HTTPException(status_code=404, detail="Workout not found")
    return None