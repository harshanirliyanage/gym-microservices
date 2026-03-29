from fastapi import FastAPI, HTTPException
from models import Equipment, EquipmentCreate, EquipmentUpdate
from service import equipment_service

app = FastAPI(
    title="Equipment Service",
    description="Manages gym equipment inventory and condition tracking",
    version="1.0.0",
)


@app.get("/api/equipment", response_model=list[Equipment], tags=["Equipment"])
def get_all_equipment():
    """Retrieve all equipment records."""
    return equipment_service.list_all()


@app.get("/api/equipment/{equipment_id}", response_model=Equipment, tags=["Equipment"])
def get_equipment(equipment_id: int):
    """Retrieve a single equipment item by ID."""
    item = equipment_service.get_one(equipment_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Equipment ID {equipment_id} not found")
    return item


@app.post("/api/equipment", response_model=Equipment, status_code=201, tags=["Equipment"])
def create_equipment(data: EquipmentCreate):
    """Add new equipment to inventory."""
    return equipment_service.add(data)


@app.put("/api/equipment/{equipment_id}", response_model=Equipment, tags=["Equipment"])
def update_equipment(equipment_id: int, data: EquipmentUpdate):
    """Update existing equipment info."""
    item = equipment_service.modify(equipment_id, data)
    if not item:
        raise HTTPException(status_code=404, detail=f"Equipment ID {equipment_id} not found")
    return item


@app.delete("/api/equipment/{equipment_id}", tags=["Equipment"])
def delete_equipment(equipment_id: int):
    """Remove equipment from inventory."""
    success = equipment_service.remove(equipment_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Equipment ID {equipment_id} not found")
    return {"message": f"Equipment ID {equipment_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)