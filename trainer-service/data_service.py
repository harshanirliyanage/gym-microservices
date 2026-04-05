# trainer-service/data_service.py
from sqlalchemy.orm import Session
from db_models import TrainerDB
from models import TrainerCreate, TrainerUpdate

class TrainerDataService:

    def get_all_trainers(self, db: Session):
        return db.query(TrainerDB).all()

    def get_trainer_by_id(self, db: Session, trainer_id: int):
        return db.query(TrainerDB).filter(
            TrainerDB.id == trainer_id
        ).first()

    def add_trainer(self, db: Session, trainer_data: TrainerCreate):
        new_trainer = TrainerDB(
            name=trainer_data.name,
            age=trainer_data.age,
            gender=trainer_data.gender,
            specialization=trainer_data.specialization,
            experience_years=trainer_data.experience_years,
            phone=trainer_data.phone,
            email=trainer_data.email,
            availability=trainer_data.availability,
            certification=trainer_data.certification
        )
        db.add(new_trainer)
        db.commit()
        db.refresh(new_trainer)
        return new_trainer

    def update_trainer(self, db: Session,
                       trainer_id: int, trainer_data: TrainerUpdate):
        trainer = self.get_trainer_by_id(db, trainer_id)
        if trainer:
            update_data = trainer_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(trainer, key, value)
            db.commit()
            db.refresh(trainer)
            return trainer
        return None

    def delete_trainer(self, db: Session, trainer_id: int):
        trainer = self.get_trainer_by_id(db, trainer_id)
        if trainer:
            db.delete(trainer)
            db.commit()
            return True
        return False