# member-service/data_service.py
from models import Member

class MemberMockDataService:
    def __init__(self):
        self.members = [
            Member(id=1, name="Raveesha Silva", age=24,
                   gender="female", email="raveesha@gym.com",
                   phone="0771234567", membership_type="Monthly",
                   membership_status="Active",
                   assigned_trainer_id=1,
                   assigned_workout_id=1,
                   weight=55.0, height=165.0),
            Member(id=2, name="Kasun Perera", age=30,
                   gender="male", email="kasun@gym.com",
                   phone="0777654321", membership_type="Annual",
                   membership_status="Active",
                   assigned_trainer_id=2,
                   assigned_workout_id=2,
                   weight=75.0, height=175.0),
            Member(id=3, name="Nimasha Fernando", age=22,
                   gender="female", email="nimasha@gym.com",
                   phone="0712345678", membership_type="Daily",
                   membership_status="Inactive",
                   assigned_trainer_id=None,
                   assigned_workout_id=None,
                   weight=50.0, height=160.0),
        ]
        self.next_id = 4

    def get_all_members(self):
        return self.members

    def get_member_by_id(self, member_id: int):
        return next((m for m in self.members if m.id == member_id), None)

    def get_members_by_status(self, status: str):
        return [m for m in self.members
                if m.membership_status.lower() == status.lower()]

    def add_member(self, member_data):
        new_member = Member(
            id=self.next_id,
            membership_status="Active",
            **member_data.dict()
        )
        self.members.append(new_member)
        self.next_id += 1
        return new_member

    def update_member(self, member_id: int, member_data):
        member = self.get_member_by_id(member_id)
        if member:
            update_data = member_data.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(member, key, value)
            return member
        return None

    def assign_trainer(self, member_id: int, trainer_id: int):
        member = self.get_member_by_id(member_id)
        if member:
            member.assigned_trainer_id = trainer_id
            return member
        return None

    def assign_workout(self, member_id: int, workout_id: int):
        member = self.get_member_by_id(member_id)
        if member:
            member.assigned_workout_id = workout_id
            return member
        return None

    def remove_trainer(self, member_id: int):
        member = self.get_member_by_id(member_id)
        if member:
            member.assigned_trainer_id = None
            return member
        return None

    def remove_workout(self, member_id: int):
        member = self.get_member_by_id(member_id)
        if member:
            member.assigned_workout_id = None
            return member
        return None

    def delete_member(self, member_id: int):
        member = self.get_member_by_id(member_id)
        if member:
            self.members.remove(member)
            return True
        return False