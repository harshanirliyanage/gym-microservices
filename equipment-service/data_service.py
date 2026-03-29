from models import Equipment, EquipmentCreate, EquipmentUpdate
from typing import Optional

# Mock database
_equipment_db: dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Treadmill",
        "category": "cardio",
        "quantity": 5,
        "condition": "good",
        "purchase_year": 2021,
    },
    2: {
        "id": 2,
        "name": "Bench Press",
        "category": "strength",
        "quantity": 3,
        "condition": "excellent",
        "purchase_year": 2022,
    },
    3: {
        "id": 3,
        "name": "Yoga Mat",
        "category": "flexibility",
        "quantity": 20,
        "condition": "fair",
        "purchase_year": 2020,
    },
    4: {
        "id": 4,
        "name": "Dumbbell Set",
        "category": "free_weights",
        "quantity": 10,
        "condition": "good",
        "purchase_year": 2019,
    },
}

_next_id: int = 5


def get_all_equipment() -> list[Equipment]:
    return [Equipment(**item) for item in _equipment_db.values()]


def get_equipment_by_id(equipment_id: int) -> Optional[Equipment]:
    item = _equipment_db.get(equipment_id)
    return Equipment(**item) if item else None


def create_equipment(data: EquipmentCreate) -> Equipment:
    global _next_id
    new_equipment = Equipment(id=_next_id, **data.model_dump())
    _equipment_db[_next_id] = new_equipment.model_dump()
    _next_id += 1
    return new_equipment


def update_equipment(equipment_id: int, data: EquipmentUpdate) -> Optional[Equipment]:
    if equipment_id not in _equipment_db:
        return None
    existing = _equipment_db[equipment_id]
    updates = data.model_dump(exclude_unset=True)
    existing.update(updates)
    _equipment_db[equipment_id] = existing
    return Equipment(**existing)


def delete_equipment(equipment_id: int) -> bool:
    if equipment_id not in _equipment_db:
        return False
    del _equipment_db[equipment_id]
    return True