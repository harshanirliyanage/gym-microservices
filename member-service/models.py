# member-service/models.py
from pydantic import BaseModel
from typing import Optional

class Member(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    email: str
    phone: str
    membership_type: str
    membership_status: str
    assigned_trainer_id: Optional[int] = None
    assigned_workout_id: Optional[int] = None
    weight: float
    height: float

class MemberCreate(BaseModel):
    name: str
    age: int
    gender: str
    email: str
    phone: str
    membership_type: str        # Monthly / Annual / Daily
    weight: float
    height: float
    # Optional — can assign during registration OR later
    assigned_trainer_id: Optional[int] = None
    assigned_workout_id: Optional[int] = None

class MemberUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    membership_type: Optional[str] = None
    membership_status: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None

class AssignTrainer(BaseModel):
    trainer_id: int

class AssignWorkout(BaseModel):
    workout_id: int