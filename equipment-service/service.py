from sqlalchemy.orm import Session
from models import EquipmentCreate, EquipmentUpdate
from data_service import EquipmentDataService

data_service = EquipmentDataService()

class EquipmentService:

    def list_all(self, db: Session):
        return data_service.get_all_equipment(db)

    def get_one(self, db: Session, equipment_id: int):
        return data_service.get_equipment_by_id(db, equipment_id)

    def get_by_category(self, db: Session, category: str):
        return data_service.get_equipment_by_category(db, category)

    def get_by_condition(self, db: Session, condition: str):
        return data_service.get_equipment_by_condition(db, condition)

    def add(self, db: Session, data: EquipmentCreate):
        return data_service.add_equipment(db, data)

    def modify(self, db: Session, equipment_id: int, data: EquipmentUpdate):
        return data_service.update_equipment(db, equipment_id, data)

    def remove(self, db: Session, equipment_id: int):
        return data_service.delete_equipment(db, equipment_id)

equipment_service = EquipmentService()