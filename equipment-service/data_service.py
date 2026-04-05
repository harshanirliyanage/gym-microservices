from sqlalchemy.orm import Session
from db_models import EquipmentDB
from models import EquipmentCreate, EquipmentUpdate

class EquipmentDataService:

    def get_all_equipment(self, db: Session):
        return db.query(EquipmentDB).all()

    def get_equipment_by_id(self, db: Session, equipment_id: int):
        return db.query(EquipmentDB).filter(
            EquipmentDB.id == equipment_id
        ).first()

    def get_equipment_by_category(self, db: Session, category: str):
        return db.query(EquipmentDB).filter(
            EquipmentDB.category == category
        ).all()

    def get_equipment_by_condition(self, db: Session, condition: str):
        return db.query(EquipmentDB).filter(
            EquipmentDB.condition == condition
        ).all()

    def add_equipment(self, db: Session, equipment_data: EquipmentCreate):
        new_equipment = EquipmentDB(
            name=equipment_data.name,
            category=equipment_data.category,
            quantity=equipment_data.quantity,
            condition=equipment_data.condition,
            purchase_year=equipment_data.purchase_year
        )
        db.add(new_equipment)
        db.commit()
        db.refresh(new_equipment)
        return new_equipment

    def update_equipment(self, db: Session,
                         equipment_id: int, equipment_data: EquipmentUpdate):
        equipment = self.get_equipment_by_id(db, equipment_id)
        if equipment:
            update_data = equipment_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(equipment, key, value)
            db.commit()
            db.refresh(equipment)
            return equipment
        return None

    def delete_equipment(self, db: Session, equipment_id: int):
        equipment = self.get_equipment_by_id(db, equipment_id)
        if equipment:
            db.delete(equipment)
            db.commit()
            return True
        return False