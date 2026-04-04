# member-service/service.py
from sqlalchemy.orm import Session
from data_service import MemberDataService
from models import MemberCreate, MemberUpdate

class MemberService:
    def __init__(self):
        self.data_service = MemberDataService()

    def get_all(self, db: Session):
        return self.data_service.get_all_members(db)

    def get_by_id(self, db: Session, member_id: int):
        return self.data_service.get_member_by_id(db, member_id)

    def get_by_status(self, db: Session, status: str):
        return self.data_service.get_members_by_status(db, status)

    def create(self, db: Session, member_data: MemberCreate):
        return self.data_service.add_member(db, member_data)

    def update(self, db: Session,
               member_id: int, member_data: MemberUpdate):
        return self.data_service.update_member(db, member_id, member_data)

    def assign_trainer(self, db: Session,
                       member_id: int, trainer_id: int):
        return self.data_service.assign_trainer(db, member_id, trainer_id)

    def assign_workout(self, db: Session,
                       member_id: int, workout_id: int):
        return self.data_service.assign_workout(db, member_id, workout_id)

    def remove_trainer(self, db: Session, member_id: int):
        return self.data_service.remove_trainer(db, member_id)

    def remove_workout(self, db: Session, member_id: int):
        return self.data_service.remove_workout(db, member_id)

    def delete(self, db: Session, member_id: int):
        return self.data_service.delete_member(db, member_id)