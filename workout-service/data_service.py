from typing import List, Optional, Dict
from models import WorkoutResponse

# In-memory mock database
_workouts_db: Dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Full Body Burn",
        "category": "Strength",
        "difficulty": "Intermediate",
        "duration_minutes": 45,
        "calories_burned": 350,
        "exercises": ["Push-ups", "Squats", "Plank", "Lunges", "Dumbbell Rows"],
        "description": "A full body strength workout targeting all major muscle groups.",
        "trainer_id": 1
    },
    2: {
        "id": 2,
        "name": "Cardio Blast",
        "category": "Cardio",
        "difficulty": "Beginner",
        "duration_minutes": 30,
        "calories_burned": 280,
        "exercises": ["Jumping Jacks", "High Knees", "Burpees", "Mountain Climbers"],
        "description": "High energy cardio session designed to boost endurance and burn fat.",
        "trainer_id": 2
    },
    3: {
        "id": 3,
        "name": "HIIT Extreme",
        "category": "HIIT",
        "difficulty": "Advanced",
        "duration_minutes": 60,
        "calories_burned": 500,
        "exercises": ["Sprint Intervals", "Box Jumps", "Kettlebell Swings", "Battle Ropes", "Sled Push"],
        "description": "An intense HIIT session for experienced athletes looking to push their limits.",
        "trainer_id": 1
    },
    4: {
        "id": 4,
        "name": "Morning Yoga Flow",
        "category": "Yoga",
        "difficulty": "Beginner",
        "duration_minutes": 40,
        "calories_burned": 150,
        "exercises": ["Sun Salutation", "Warrior I", "Warrior II", "Child's Pose", "Downward Dog"],
        "description": "A calming morning yoga routine to improve flexibility and mindfulness.",
        "trainer_id": 3
    },
    5: {
        "id": 5,
        "name": "Power Flex",
        "category": "Flexibility",
        "difficulty": "Intermediate",
        "duration_minutes": 35,
        "calories_burned": 180,
        "exercises": ["Dynamic Stretching", "Hip Flexor Stretch", "Hamstring Stretch", "Shoulder Mobility"],
        "description": "Improve your range of motion and reduce injury risk with this flexibility plan.",
        "trainer_id": 2
    }
}

_next_id: int = 6


def get_all_workouts() -> List[dict]:
    return list(_workouts_db.values())


def get_workout_by_id(workout_id: int) -> Optional[dict]:
    return _workouts_db.get(workout_id)


def create_workout(workout_data: dict) -> dict:
    global _next_id
    new_workout = {"id": _next_id, **workout_data}
    _workouts_db[_next_id] = new_workout
    _next_id += 1
    return new_workout


def update_workout(workout_id: int, update_data: dict) -> Optional[dict]:
    if workout_id not in _workouts_db:
        return None
    existing = _workouts_db[workout_id]
    for key, value in update_data.items():
        if value is not None:
            existing[key] = value
    _workouts_db[workout_id] = existing
    return existing


def delete_workout(workout_id: int) -> bool:
    if workout_id not in _workouts_db:
        return False
    del _workouts_db[workout_id]
    return True
