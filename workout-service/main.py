from fastapi import FastAPI, HTTPException, status
from typing import List
from models import WorkoutCreate, WorkoutUpdate, WorkoutResponse
import service

app = FastAPI(
    title="Workout Service API",
    description="Microservice for managing gym workout plans - Developed by Pabasara",
    version="1.0.0"
)


@app.get("/", tags=["Health"])
def root():
    return {"service": "Workout Service", "status": "running", "developer": "Pabasara", "port": 8003}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "service": "workout-service"}


# ─────────────────────────────────────────────
# WORKOUT ENDPOINTS
# ─────────────────────────────────────────────

@app.get(
    "/api/workouts",
    response_model=List[WorkoutResponse],
    tags=["Workouts"],
    summary="Get all workout plans",
    description="Retrieve a list of all available workout plans in the gym system."
)
def get_all_workouts():
    workouts = service.get_all_workouts()
    return workouts


@app.get(
    "/api/workouts/{workout_id}",
    response_model=WorkoutResponse,
    tags=["Workouts"],
    summary="Get a workout by ID",
    description="Retrieve a specific workout plan by its unique ID."
)
def get_workout(workout_id: int):
    workout = service.get_workout_by_id(workout_id)
    if not workout:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workout with ID {workout_id} not found"
        )
    return workout


@app.post(
    "/api/workouts",
    response_model=WorkoutResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Workouts"],
    summary="Create a new workout plan",
    description="Add a new workout plan to the gym system."
)
def create_workout(workout: WorkoutCreate):
    new_workout = service.create_workout(workout)
    return new_workout


@app.put(
    "/api/workouts/{workout_id}",
    response_model=WorkoutResponse,
    tags=["Workouts"],
    summary="Update an existing workout plan",
    description="Update details of an existing workout plan by its ID."
)
def update_workout(workout_id: int, workout: WorkoutUpdate):
    updated = service.update_workout(workout_id, workout)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workout with ID {workout_id} not found"
        )
    return updated


@app.delete(
    "/api/workouts/{workout_id}",
    tags=["Workouts"],
    summary="Delete a workout plan",
    description="Permanently delete a workout plan by its ID.",
    status_code=status.HTTP_200_OK
)
def delete_workout(workout_id: int):
    deleted = service.delete_workout(workout_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workout with ID {workout_id} not found"
        )
    return {"message": f"Workout with ID {workout_id} has been successfully deleted"}
