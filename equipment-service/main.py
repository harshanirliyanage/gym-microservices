from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base, SessionLocal
from models import Equipment, EquipmentCreate, EquipmentUpdate
from service import equipment_service
from db_models import EquipmentDB

# Creates equipment.db automatically on startup
Base.metadata.create_all(bind=engine)

# Seed sample data if database is empty
def seed_data():
    db = SessionLocal()
    if db.query(EquipmentDB).count() == 0:
        sample = [
            EquipmentDB(name="Treadmill", category="cardio", quantity=5, condition="good", purchase_year=2021),
            EquipmentDB(name="Bench Press", category="strength", quantity=3, condition="excellent", purchase_year=2022),
            EquipmentDB(name="Yoga Mat", category="flexibility", quantity=20, condition="fair", purchase_year=2020),
            EquipmentDB(name="Dumbbell Set", category="free_weights", quantity=10, condition="good", purchase_year=2019),
        ]
        db.add_all(sample)
        db.commit()
    db.close()

seed_data()

app = FastAPI(
    title="Equipment Microservice",
    description="Manages gym equipment inventory and condition tracking",
    version="1.0.0",
)

@app.get("/", tags=["default"])
def read_root():
    return {
        "service": "Equipment Service",
        "version": "1.0.0",
        "description": "Manages gym equipment inventory and condition tracking",
        "docs": "/docs",
        "endpoints": "/api/equipment"
    }

@app.get("/api/equipment", response_model=list[Equipment], tags=["Equipment"])
def get_all_equipment(db: Session = Depends(get_db)):
    return equipment_service.list_all(db)

@app.get("/api/equipment/{equipment_id}", response_model=Equipment, tags=["Equipment"])
def get_equipment(equipment_id: int, db: Session = Depends(get_db)):
    item = equipment_service.get_one(db, equipment_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Equipment ID {equipment_id} not found")
    return item

@app.post("/api/equipment", response_model=Equipment, status_code=201, tags=["Equipment"])
def create_equipment(data: EquipmentCreate, db: Session = Depends(get_db)):
    return equipment_service.add(db, data)

@app.put("/api/equipment/{equipment_id}", response_model=Equipment, tags=["Equipment"])
def update_equipment(equipment_id: int, data: EquipmentUpdate, db: Session = Depends(get_db)):
    item = equipment_service.modify(db, equipment_id, data)
    if not item:
        raise HTTPException(status_code=404, detail=f"Equipment ID {equipment_id} not found")
    return item

@app.delete("/api/equipment/{equipment_id}", tags=["Equipment"])
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    success = equipment_service.remove(db, equipment_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Equipment ID {equipment_id} not found")
    return {"message": f"Equipment ID {equipment_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)