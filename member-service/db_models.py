# member-service/db_models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class MemberDB(Base):
    __tablename__ = "members"

    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String, nullable=False)
    age                 = Column(Integer, nullable=False)
    gender              = Column(String, nullable=False)
    email               = Column(String, nullable=False)
    phone               = Column(String, nullable=False)
    membership_type     = Column(String, nullable=False)
    membership_status   = Column(String, default="Active")
    assigned_trainer_id = Column(Integer, nullable=True)
    assigned_workout_id = Column(Integer, nullable=True)
    weight              = Column(Float, nullable=False)
    height              = Column(Float, nullable=False)