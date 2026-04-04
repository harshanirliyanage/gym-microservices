# workout-service/db_models.py
from sqlalchemy import Column, Integer, String
from database import Base


class WorkoutDB(Base):
    __tablename__ = "workouts"

    id              = Column(Integer, primary_key=True, index=True)
    name            = Column(String, nullable=False)
    category        = Column(String, nullable=False)
    difficulty      = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    calories_burned = Column(Integer, nullable=False)
    exercises       = Column(String, nullable=False)   # stored as comma-separated string
    description     = Column(String, nullable=False)
    trainer_id      = Column(Integer, nullable=True)
