from sqlalchemy import Column, Integer, String
from database import Base

class EquipmentDB(Base):
    __tablename__ = "equipment"

    id            = Column(Integer, primary_key=True, index=True)
    name          = Column(String, nullable=False)
    category      = Column(String, nullable=False)   # cardio / strength / flexibility / free_weights
    quantity      = Column(Integer, nullable=False)
    condition     = Column(String, nullable=False)   # excellent / good / fair / needs_repair
    purchase_year = Column(Integer, nullable=False)