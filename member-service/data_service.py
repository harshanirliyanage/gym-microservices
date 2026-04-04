# member-service/data_service.py
from sqlalchemy.orm import Session
from db_models import MemberDB
from models import MemberCreate, MemberUpdate

class MemberDataService:

    def get_all_members(self, db: Session):
        return db.query(MemberDB).all()

    def get_member_by_id(self, db: Session, member_id: int):
        return db.query(MemberDB).filter(
            MemberDB.id == member_id
        ).first()

    def get_members_by_status(self, db: Session, status: str):
        return db.query(MemberDB).filter(
            MemberDB.membership_status == status
        ).all()

    def add_member(self, db: Session, member_data: MemberCreate):
        new_member = MemberDB(
            name=member_data.name,
            age=member_data.age,
            gender=member_data.gender,
            email=member_data.email,
            phone=member_data.phone,
            membership_type=member_data.membership_type,
            membership_status="Active",
            assigned_trainer_id=member_data.assigned_trainer_id,
            assigned_workout_id=member_data.assigned_workout_id,
            weight=member_data.weight,
            height=member_data.height
        )
        db.add(new_member)
        db.commit()
        db.refresh(new_member)
        return new_member

    def update_member(self, db: Session,
                      member_id: int, member_data: MemberUpdate):
        member = self.get_member_by_id(db, member_id)
        if member:
            update_data = member_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(member, key, value)
            db.commit()
            db.refresh(member)
            return member
        return None

    def assign_trainer(self, db: Session,
                       member_id: int, trainer_id: int):
        member = self.get_member_by_id(db, member_id)
        if member:
            member.assigned_trainer_id = trainer_id
            db.commit()
            db.refresh(member)
            return member
        return None

    def assign_workout(self, db: Session,
                       member_id: int, workout_id: int):
        member = self.get_member_by_id(db, member_id)
        if member:
            member.assigned_workout_id = workout_id
            db.commit()
            db.refresh(member)
            return member
        return None

    def remove_trainer(self, db: Session, member_id: int):
        member = self.get_member_by_id(db, member_id)
        if member:
            member.assigned_trainer_id = None
            db.commit()
            db.refresh(member)
            return member
        return None

    def remove_workout(self, db: Session, member_id: int):
        member = self.get_member_by_id(db, member_id)
        if member:
            member.assigned_workout_id = None
            db.commit()
            db.refresh(member)
            return member
        return None

    def delete_member(self, db: Session, member_id: int):
        member = self.get_member_by_id(db, member_id)
        if member:
            db.delete(member)
            db.commit()
            return True
        return False