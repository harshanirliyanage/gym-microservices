# member-service/main.py
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from models import Member, MemberCreate, MemberUpdate, AssignTrainer, AssignWorkout
from service import MemberService
from database import engine, get_db
import db_models
from typing import List

# Create database tables automatically
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Member Microservice", version="1.0.0")
member_service = MemberService()

@app.get("/")
def read_root():
    return {"message": "Member Microservice is running with SQLite DB!"}

# ── CRUD ──────────────────────────────────────────────────

@app.get("/api/members", response_model=List[Member])
def get_all_members(db: Session = Depends(get_db)):
    """Get all members"""
    return member_service.get_all(db)

@app.get("/api/members/status/{status}", response_model=List[Member])
def get_members_by_status(status: str,
                          db: Session = Depends(get_db)):
    """Get members by status - Active / Inactive / Suspended"""
    return member_service.get_by_status(db, status)

@app.get("/api/members/{member_id}", response_model=Member)
def get_member(member_id: int,
               db: Session = Depends(get_db)):
    """Get a member by ID"""
    member = member_service.get_by_id(db, member_id)
    if not member:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return member

@app.post("/api/members", response_model=Member,
          status_code=status.HTTP_201_CREATED)
def create_member(member: MemberCreate,
                  db: Session = Depends(get_db)):
    """Register a new gym member"""
    return member_service.create(db, member)

@app.put("/api/members/{member_id}", response_model=Member)
def update_member(member_id: int, member: MemberUpdate,
                  db: Session = Depends(get_db)):
    """Update member details"""
    updated = member_service.update(db, member_id, member)
    if not updated:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return updated

@app.delete("/api/members/{member_id}",
            status_code=status.HTTP_204_NO_CONTENT)
def delete_member(member_id: int,
                  db: Session = Depends(get_db)):
    """Remove a member"""
    success = member_service.delete(db, member_id)
    if not success:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return None

# ── ASSIGN / REMOVE ───────────────────────────────────────

@app.put("/api/members/{member_id}/assign-trainer",
         response_model=Member)
def assign_trainer(member_id: int, data: AssignTrainer,
                   db: Session = Depends(get_db)):
    """Assign a trainer to a member"""
    updated = member_service.assign_trainer(
        db, member_id, data.trainer_id)
    if not updated:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return updated

@app.put("/api/members/{member_id}/assign-workout",
         response_model=Member)
def assign_workout(member_id: int, data: AssignWorkout,
                   db: Session = Depends(get_db)):
    """Assign a workout to a member"""
    updated = member_service.assign_workout(
        db, member_id, data.workout_id)
    if not updated:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return updated

@app.put("/api/members/{member_id}/remove-trainer",
         response_model=Member)
def remove_trainer(member_id: int,
                   db: Session = Depends(get_db)):
    """Remove trainer from member"""
    updated = member_service.remove_trainer(db, member_id)
    if not updated:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return updated

@app.put("/api/members/{member_id}/remove-workout",
         response_model=Member)
def remove_workout(member_id: int,
                   db: Session = Depends(get_db)):
    """Remove workout from member"""
    updated = member_service.remove_workout(db, member_id)
    if not updated:
        raise HTTPException(status_code=404,
                            detail="Member not found")
    return updated