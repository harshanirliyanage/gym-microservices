# trainer-service/service.py
from sqlalchemy.orm import Session
from data_service import TrainerDataService
from models import TrainerCreate, TrainerUpdate

class TrainerService:
    def __init__(self):
        self.data_service = TrainerDataService()

    def get_all(self, db: Session):
        return self.data_service.get_all_trainers(db)

    def get_by_id(self, db: Session, trainer_id: int):
        return self.data_service.get_trainer_by_id(db, trainer_id)

    def create(self, db: Session, trainer_data: TrainerCreate):
        return self.data_service.add_trainer(db, trainer_data)

    def update(self, db: Session, trainer_id: int, trainer_data: TrainerUpdate):
        return self.data_service.update_trainer(db, trainer_id, trainer_data)

    def delete(self, db: Session, trainer_id: int):
        return self.data_service.delete_trainer(db, trainer_id)
