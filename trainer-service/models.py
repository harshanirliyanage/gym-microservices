# trainer_service/models.py
from pydantic import BaseModel
from typing import Optional

class Trainer(BaseModel):
    id: int
    name: str
    age: int             # trainer's age
    gender: str          # male, female
    specialization: str  # cardio, strength, yoga, crossfit
    experience_years: int
    phone: str
    email: str           # trainer contact email
    availability: str    # morning, evening, fullday
    certification: str   # ACE, NASM, ACSM

class TrainerCreate(BaseModel):
    name: str
    age: int
    gender: str
    specialization: str
    experience_years: int
    phone: str
    email: str
    availability: str
    certification: str

class TrainerUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    specialization: Optional[str] = None
    experience_years: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    availability: Optional[str] = None
    certification: Optional[str] = None