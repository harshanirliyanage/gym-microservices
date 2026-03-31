# member-service/service.py
from data_service import MemberMockDataService

class MemberService:
    def __init__(self):
        self.data_service = MemberMockDataService()

    def get_all(self):
        return self.data_service.get_all_members()

    def get_by_id(self, member_id: int):
        return self.data_service.get_member_by_id(member_id)

    def get_by_status(self, status: str):
        return self.data_service.get_members_by_status(status)

    def create(self, member_data):
        return self.data_service.add_member(member_data)

    def update(self, member_id: int, member_data):
        return self.data_service.update_member(member_id, member_data)

    def assign_trainer(self, member_id: int, trainer_id: int):
        return self.data_service.assign_trainer(member_id, trainer_id)

    def assign_workout(self, member_id: int, workout_id: int):
        return self.data_service.assign_workout(member_id, workout_id)

    def remove_trainer(self, member_id: int):
        return self.data_service.remove_trainer(member_id)

    def remove_workout(self, member_id: int):
        return self.data_service.remove_workout(member_id)

    def delete(self, member_id: int):
        return self.data_service.delete_member(member_id)