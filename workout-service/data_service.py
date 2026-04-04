# workout-service/data_service.py
from sqlalchemy.orm import Session
from db_models import WorkoutDB
from models import WorkoutCreate, WorkoutUpdate, WorkoutCategory, DifficultyLevel


# ── Helper: convert exercises list ↔ string ──────────────
def list_to_str(exercises: list) -> str:
    return ",".join(exercises)

def str_to_list(exercises_str: str) -> list:
    return [e.strip() for e in exercises_str.split(",")]

def db_to_dict(workout: WorkoutDB) -> dict:
    """Convert DB row to dict with exercises as list"""
    return {
        "id": workout.id,
        "name": workout.name,
        "category": workout.category,
        "difficulty": workout.difficulty,
        "duration_minutes": workout.duration_minutes,
        "calories_burned": workout.calories_burned,
        "exercises": str_to_list(workout.exercises),
        "description": workout.description,
        "trainer_id": workout.trainer_id,
    }


# ── Seed initial data if table is empty ──────────────────
def seed_data(db: Session):
    if db.query(WorkoutDB).count() == 0:
        initial_workouts = [
            WorkoutDB(
                name="Full Body Burn",
                category=WorkoutCategory.strength.value,
                difficulty=DifficultyLevel.intermediate.value,
                duration_minutes=45,
                calories_burned=350,
                exercises="Push-ups,Squats,Plank,Lunges,Dumbbell Rows",
                description="A full body strength workout targeting all major muscle groups.",
                trainer_id=1
            ),
            WorkoutDB(
                name="Cardio Blast",
                category=WorkoutCategory.cardio.value,
                difficulty=DifficultyLevel.beginner.value,
                duration_minutes=30,
                calories_burned=280,
                exercises="Jumping Jacks,High Knees,Burpees,Mountain Climbers",
                description="High energy cardio session designed to boost endurance and burn fat.",
                trainer_id=2
            ),
            WorkoutDB(
                name="HIIT Extreme",
                category=WorkoutCategory.hiit.value,
                difficulty=DifficultyLevel.advanced.value,
                duration_minutes=60,
                calories_burned=500,
                exercises="Sprint Intervals,Box Jumps,Kettlebell Swings,Battle Ropes",
                description="An intense HIIT session for experienced athletes.",
                trainer_id=1
            ),
            WorkoutDB(
                name="Morning Yoga Flow",
                category=WorkoutCategory.yoga.value,
                difficulty=DifficultyLevel.beginner.value,
                duration_minutes=40,
                calories_burned=150,
                exercises="Sun Salutation,Warrior I,Warrior II,Child's Pose,Downward Dog",
                description="A calming morning yoga routine to improve flexibility.",
                trainer_id=3
            ),
            WorkoutDB(
                name="Power Flex",
                category=WorkoutCategory.flexibility.value,
                difficulty=DifficultyLevel.intermediate.value,
                duration_minutes=35,
                calories_burned=180,
                exercises="Dynamic Stretching,Hip Flexor Stretch,Hamstring Stretch,Shoulder Mobility",
                description="Improve your range of motion and reduce injury risk.",
                trainer_id=2
            ),
        ]
        db.add_all(initial_workouts)
        db.commit()


# ── CRUD Operations ───────────────────────────────────────

def get_all_workouts(db: Session):
    workouts = db.query(WorkoutDB).all()
    return [db_to_dict(w) for w in workouts]


def get_workout_by_id(db: Session, workout_id: int):
    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()
    if not workout:
        return None
    return db_to_dict(workout)


def create_workout(db: Session, workout_data: WorkoutCreate):
    new_workout = WorkoutDB(
        name=workout_data.name,
        category=workout_data.category.value,
        difficulty=workout_data.difficulty.value,
        duration_minutes=workout_data.duration_minutes,
        calories_burned=workout_data.calories_burned,
        exercises=list_to_str(workout_data.exercises),
        description=workout_data.description,
        trainer_id=workout_data.trainer_id
    )
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return db_to_dict(new_workout)


def update_workout(db: Session, workout_id: int, workout_data: WorkoutUpdate):
    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()
    if not workout:
        return None
    if workout_data.name is not None:
        workout.name = workout_data.name
    if workout_data.category is not None:
        workout.category = workout_data.category.value
    if workout_data.difficulty is not None:
        workout.difficulty = workout_data.difficulty.value
    if workout_data.duration_minutes is not None:
        workout.duration_minutes = workout_data.duration_minutes
    if workout_data.calories_burned is not None:
        workout.calories_burned = workout_data.calories_burned
    if workout_data.exercises is not None:
        workout.exercises = list_to_str(workout_data.exercises)
    if workout_data.description is not None:
        workout.description = workout_data.description
    if workout_data.trainer_id is not None:
        workout.trainer_id = workout_data.trainer_id
    db.commit()
    db.refresh(workout)
    return db_to_dict(workout)


def delete_workout(db: Session, workout_id: int):
    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()
    if not workout:
        return False
    db.delete(workout)
    db.commit()
    return True