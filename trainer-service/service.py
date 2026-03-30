# trainer_service/service.py
from data_service import TrainerMockDataService

class TrainerService:
    def __init__(self):
        self.data_service = TrainerMockDataService()

    def get_all(self):
        return self.data_service.get_all_trainers()

    def get_by_id(self, trainer_id: int):
        return self.data_service.get_trainer_by_id(trainer_id)

    def create(self, trainer_data):
        return self.data_service.add_trainer(trainer_data)

    def update(self, trainer_id: int, trainer_data):
        return self.data_service.update_trainer(trainer_id, trainer_data)

    def delete(self, trainer_id: int):
        return self.data_service.delete_trainer(trainer_id)
