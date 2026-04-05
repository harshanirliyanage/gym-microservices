# trainer-service/main.py
from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from models import Trainer, TrainerCreate, TrainerUpdate
from service import TrainerService
from database import engine, get_db
import db_models
from typing import List

# Create database tables automatically
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Trainer Microservice", version="1.0.0")
trainer_service = TrainerService()

@app.get("/")
def read_root():
    return {"message": "Trainer Microservice is running with SQLite DB!"}

# ── CRUD ──────────────────────────────────────────────────

@app.get("/api/trainers", response_model=List[Trainer])
def get_all_trainers(db: Session = Depends(get_db)):
    """Get all trainers"""
    return trainer_service.get_all(db)

@app.get("/api/trainers/{trainer_id}", response_model=Trainer)
def get_trainer(trainer_id: int,
                db: Session = Depends(get_db)):
    """Get a trainer by ID"""
    trainer = trainer_service.get_by_id(db, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404,
                            detail="Trainer not found")
    return trainer

@app.post("/api/trainers", response_model=Trainer,
          status_code=status.HTTP_201_CREATED)
def create_trainer(trainer: TrainerCreate,
                   db: Session = Depends(get_db)):
    """Register a new gym trainer"""
    return trainer_service.create(db, trainer)

@app.put("/api/trainers/{trainer_id}", response_model=Trainer)
def update_trainer(trainer_id: int, trainer: TrainerUpdate,
                   db: Session = Depends(get_db)):
    """Update trainer details"""
    updated = trainer_service.update(db, trainer_id, trainer)
    if not updated:
        raise HTTPException(status_code=404,
                            detail="Trainer not found")
    return updated

@app.delete("/api/trainers/{trainer_id}",
            status_code=status.HTTP_204_NO_CONTENT)
def delete_trainer(trainer_id: int,
                   db: Session = Depends(get_db)):
    """Remove a trainer"""
    success = trainer_service.delete(db, trainer_id)
    if not success:
        raise HTTPException(status_code=404,
                            detail="Trainer not found")
    return None
