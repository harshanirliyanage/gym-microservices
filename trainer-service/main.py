# trainer_service/main.py
from fastapi import FastAPI, HTTPException, status
from models import Trainer, TrainerCreate, TrainerUpdate
from service import TrainerService
from typing import List

app = FastAPI(title="Trainer Microservice", version="1.0.0")

trainer_service = TrainerService()

@app.get("/")
def read_root():
    return {"message": "Trainer Microservice is running"}

@app.get("/api/trainers", response_model=List[Trainer])
def get_all_trainers():
    """Get all gym trainers"""
    return trainer_service.get_all()

@app.get("/api/trainers/{trainer_id}", response_model=Trainer)
def get_trainer(trainer_id: int):
    """Get a trainer by ID"""
    trainer = trainer_service.get_by_id(trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer

@app.post("/api/trainers", response_model=Trainer, status_code=status.HTTP_201_CREATED)
def create_trainer(trainer: TrainerCreate):
    """Add a new trainer"""
    return trainer_service.create(trainer)

@app.put("/api/trainers/{trainer_id}", response_model=Trainer)
def update_trainer(trainer_id: int, trainer: TrainerUpdate):
    """Update trainer details"""
    updated_trainer = trainer_service.update(trainer_id, trainer)
    if not updated_trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return updated_trainer

@app.delete("/api/trainers/{trainer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trainer(trainer_id: int):
    """Delete a trainer"""
    success = trainer_service.delete(trainer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return None
