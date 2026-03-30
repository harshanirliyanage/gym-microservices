from typing import List, Optional
from models import WorkoutCreate, WorkoutUpdate, WorkoutResponse
import data_service


def get_all_workouts() -> List[WorkoutResponse]:
    workouts = data_service.get_all_workouts()
    return [WorkoutResponse(**w) for w in workouts]


def get_workout_by_id(workout_id: int) -> Optional[WorkoutResponse]:
    workout = data_service.get_workout_by_id(workout_id)
    if not workout:
        return None
    return WorkoutResponse(**workout)


def create_workout(workout_data: WorkoutCreate) -> WorkoutResponse:
    data_dict = workout_data.model_dump()
    # Convert enums to their string values
    data_dict["category"] = data_dict["category"].value if hasattr(data_dict["category"], "value") else data_dict["category"]
    data_dict["difficulty"] = data_dict["difficulty"].value if hasattr(data_dict["difficulty"], "value") else data_dict["difficulty"]
    new_workout = data_service.create_workout(data_dict)
    return WorkoutResponse(**new_workout)


def update_workout(workout_id: int, update_data: WorkoutUpdate) -> Optional[WorkoutResponse]:
    existing = data_service.get_workout_by_id(workout_id)
    if not existing:
        return None
    update_dict = {k: v for k, v in update_data.model_dump().items() if v is not None}
    # Convert enums to string values
    if "category" in update_dict and hasattr(update_dict["category"], "value"):
        update_dict["category"] = update_dict["category"].value
    if "difficulty" in update_dict and hasattr(update_dict["difficulty"], "value"):
        update_dict["difficulty"] = update_dict["difficulty"].value
    updated = data_service.update_workout(workout_id, update_dict)
    return WorkoutResponse(**updated)


def delete_workout(workout_id: int) -> bool:
    return data_service.delete_workout(workout_id)
