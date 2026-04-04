# workout-service/service.py
from sqlalchemy.orm import Session
from models import WorkoutCreate, WorkoutUpdate
import data_service


class WorkoutService:

    def get_all(self, db: Session):
        return data_service.get_all_workouts(db)

    def get_by_id(self, db: Session, workout_id: int):
        return data_service.get_workout_by_id(db, workout_id)

    def create(self, db: Session, workout_data: WorkoutCreate):
        return data_service.create_workout(db, workout_data)

    def update(self, db: Session, workout_id: int, workout_data: WorkoutUpdate):
        return data_service.update_workout(db, workout_id, workout_data)

    def delete(self, db: Session, workout_id: int):
        return data_service.delete_workout(db, workout_id)
