from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class CategoryEnum(str, Enum):
    cardio = "cardio"
    strength = "strength"
    flexibility = "flexibility"
    free_weights = "free_weights"


class ConditionEnum(str, Enum):
    excellent = "excellent"
    good = "good"
    fair = "fair"
    needs_repair = "needs_repair"


class Equipment(BaseModel):
    id: int
    name: str
    category: CategoryEnum
    quantity: int
    condition: ConditionEnum
    purchase_year: int


class EquipmentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: CategoryEnum
    quantity: int = Field(..., gt=0)
    condition: ConditionEnum
    purchase_year: int = Field(..., ge=1900, le=2100)


class EquipmentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    category: Optional[CategoryEnum] = None
    quantity: Optional[int] = Field(None, gt=0)
    condition: Optional[ConditionEnum] = None
    purchase_year: Optional[int] = Field(None, ge=1900, le=2100)