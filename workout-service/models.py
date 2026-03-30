from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class DifficultyLevel(str, Enum):
    beginner = "Beginner"
    intermediate = "Intermediate"
    advanced = "Advanced"


class WorkoutCategory(str, Enum):
    cardio = "Cardio"
    strength = "Strength"
    flexibility = "Flexibility"
    hiit = "HIIT"
    yoga = "Yoga"
    crossfit = "CrossFit"


class WorkoutCreate(BaseModel):
    name: str = Field(..., example="Full Body Burn")
    category: WorkoutCategory = Field(..., example="Strength")
    difficulty: DifficultyLevel = Field(..., example="Intermediate")
    duration_minutes: int = Field(..., gt=0, example=45)
    calories_burned: int = Field(..., gt=0, example=350)
    exercises: List[str] = Field(..., example=["Push-ups", "Squats", "Plank", "Lunges"])
    description: str = Field(..., example="A full body strength workout targeting all major muscle groups")
    trainer_id: Optional[int] = Field(None, example=1)


class WorkoutUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Full Body Burn v2")
    category: Optional[WorkoutCategory] = Field(None, example="Strength")
    difficulty: Optional[DifficultyLevel] = Field(None, example="Advanced")
    duration_minutes: Optional[int] = Field(None, gt=0, example=60)
    calories_burned: Optional[int] = Field(None, gt=0, example=420)
    exercises: Optional[List[str]] = Field(None, example=["Push-ups", "Deadlifts", "Plank"])
    description: Optional[str] = Field(None, example="Updated full body strength workout")
    trainer_id: Optional[int] = Field(None, example=2)


class WorkoutResponse(BaseModel):
    id: int
    name: str
    category: WorkoutCategory
    difficulty: DifficultyLevel
    duration_minutes: int
    calories_burned: int
    exercises: List[str]
    description: str
    trainer_id: Optional[int]

    class Config:
        from_attributes = True
