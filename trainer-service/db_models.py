# trainer-service/db_models.py
from sqlalchemy import Column, Integer, String
from database import Base

class TrainerDB(Base):
    __tablename__ = "trainers"

    id                  = Column(Integer, primary_key=True, index=True)
    name                = Column(String, nullable=False)
    age                 = Column(Integer, nullable=False)
    gender              = Column(String, nullable=False)
    specialization      = Column(String, nullable=False)
    experience_years    = Column(Integer, nullable=False)
    phone               = Column(String, nullable=False)
    email               = Column(String, nullable=False)
    availability        = Column(String, nullable=False)
    certification       = Column(String, nullable=False)
