# member-service/models.py
from pydantic import BaseModel
from typing import Optional

class Member(BaseModel):
    id: int
    name: str
    age: int
    email: str
    membership_type: str
    phone: str

class MemberCreate(BaseModel):
    name: str
    age: int
    email: str
    membership_type: str
    phone: str

class MemberUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    membership_type: Optional[str] = None
    phone: Optional[str] = None