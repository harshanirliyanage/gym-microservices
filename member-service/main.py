# member-service/main.py
from fastapi import FastAPI, HTTPException, status
from models import Member, MemberCreate, MemberUpdate, AssignTrainer, AssignWorkout
from service import MemberService
from typing import List

app = FastAPI(title="Member Microservice", version="1.0.0")
member_service = MemberService()

@app.get("/")
def read_root():
    return {"message": "Member Microservice is running"}

# ── CRUD ──────────────────────────────────────────────────────

@app.get("/api/members", response_model=List[Member])
def get_all_members():
    """Get all members"""
    return member_service.get_all()

@app.get("/api/members/status/{status}", response_model=List[Member])
def get_members_by_status(status: str):
    """Get members by status - Active / Inactive / Suspended"""
    return member_service.get_by_status(status)

@app.get("/api/members/{member_id}", response_model=Member)
def get_member(member_id: int):
    """Get a member by ID"""
    member = member_service.get_by_id(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.post("/api/members", response_model=Member,
          status_code=status.HTTP_201_CREATED)
def create_member(member: MemberCreate):
    """Register a new gym member
    - Can optionally assign trainer and workout during registration
    """
    return member_service.create(member)

@app.put("/api/members/{member_id}", response_model=Member)
def update_member(member_id: int, member: MemberUpdate):
    """Update member details or membership status"""
    updated = member_service.update(member_id, member)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated

@app.delete("/api/members/{member_id}",
            status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: int):
    """Remove a member from the gym"""
    success = member_service.delete(member_id)
    if not success:
        raise HTTPException(status_code=404, detail="Member not found")
    return None

# ── ASSIGN / REMOVE ───────────────────────────────────────────

@app.put("/api/members/{member_id}/assign-trainer",
         response_model=Member)
def assign_trainer(member_id: int, data: AssignTrainer):
    """Assign a trainer to a member"""
    updated = member_service.assign_trainer(member_id, data.trainer_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated

@app.put("/api/members/{member_id}/assign-workout",
         response_model=Member)
def assign_workout(member_id: int, data: AssignWorkout):
    """Assign a workout plan to a member"""
    updated = member_service.assign_workout(member_id, data.workout_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated

@app.put("/api/members/{member_id}/remove-trainer",
         response_model=Member)
def remove_trainer(member_id: int):
    """Remove assigned trainer from member"""
    updated = member_service.remove_trainer(member_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated

@app.put("/api/members/{member_id}/remove-workout",
         response_model=Member)
def remove_workout(member_id: int):
    """Remove assigned workout from member"""
    updated = member_service.remove_workout(member_id)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated