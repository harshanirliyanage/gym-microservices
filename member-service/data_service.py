# member-service/data_service.py
from models import Member

class MemberMockDataService:
    def __init__(self):
        self.members = [
            Member(id=1, name="Raveesha Silva", age=24, email="raveesha@gym.com",
                   membership_type="Monthly", phone="0771234567"),
            Member(id=2, name="Kasun Perera", age=30, email="kasun@gym.com",
                   membership_type="Annual", phone="0777654321"),
            Member(id=3, name="Nimasha Fernando", age=22, email="nimasha@gym.com",
                   membership_type="Daily", phone="0712345678"),
        ]
        self.next_id = 4

    def get_all_members(self):
        return self.members

    def get_member_by_id(self, member_id: int):
        return next((m for m in self.members if m.id == member_id), None)

    def add_member(self, member_data):
        new_member = Member(id=self.next_id, **member_data.dict())
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

    def delete_member(self, member_id: int):
        member = self.get_member_by_id(member_id)
        if member:
            self.members.remove(member)
            return True
        return False