# member-service/main.py
from fastapi import FastAPI, HTTPException, status
from models import Member, MemberCreate, MemberUpdate
from service import MemberService
from typing import List

app = FastAPI(title="Member Microservice", version="1.0.0")

member_service = MemberService()

@app.get("/")
def read_root():
    return {"message": "Member Microservice is running"}

@app.get("/api/members", response_model=List[Member])
def get_all_members():
    """Get all members"""
    return member_service.get_all()

@app.get("/api/members/{member_id}", response_model=Member)
def get_member(member_id: int):
    """Get a member by ID"""
    member = member_service.get_by_id(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.post("/api/members", response_model=Member, status_code=status.HTTP_201_CREATED)
def create_member(member: MemberCreate):
    """Create a new member"""
    return member_service.create(member)

@app.put("/api/members/{member_id}", response_model=Member)
def update_member(member_id: int, member: MemberUpdate):
    """Update a member"""
    updated = member_service.update(member_id, member)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated

@app.delete("/api/members/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: int):
    """Delete a member"""
    success = member_service.delete(member_id)
    if not success:
        raise HTTPException(status_code=404, detail="Member not found")
    return None