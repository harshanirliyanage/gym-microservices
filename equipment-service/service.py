from models import Equipment, EquipmentCreate, EquipmentUpdate
from data_service import (
    get_all_equipment,
    get_equipment_by_id,
    create_equipment,
    update_equipment,
    delete_equipment,
)
from typing import Optional


class EquipmentService:

    def list_all(self) -> list[Equipment]:
        return get_all_equipment()

    def get_one(self, equipment_id: int) -> Optional[Equipment]:
        return get_equipment_by_id(equipment_id)

    def add(self, data: EquipmentCreate) -> Equipment:
        return create_equipment(data)

    def modify(self, equipment_id: int, data: EquipmentUpdate) -> Optional[Equipment]:
        return update_equipment(equipment_id, data)

    def remove(self, equipment_id: int) -> bool:
        return delete_equipment(equipment_id)


equipment_service = EquipmentService()