# trainer_service/data_service.py
from models import Trainer

class TrainerMockDataService:
    def __init__(self):
        self.trainers = [
            Trainer(id=1,  name="Roshan Bandara",     age=30, gender="male",   specialization="strength", experience_years=5,  phone="0711234567", email="roshan@gym.com",   availability="morning", certification="ACE"),
            Trainer(id=2,  name="Priya Kumari",       age=27, gender="female", specialization="yoga",     experience_years=3,  phone="0719876543", email="priya@gym.com",    availability="evening", certification="NASM"),
            Trainer(id=3,  name="Asanka Jayawardena", age=35, gender="male",   specialization="cardio",   experience_years=7,  phone="0755432109", email="asanka@gym.com",   availability="fullday", certification="ACSM"),
            Trainer(id=4,  name="Nimasha Perera",     age=26, gender="female", specialization="crossfit", experience_years=2,  phone="0762345678", email="nimasha@gym.com",  availability="morning", certification="ACE"),
            Trainer(id=5,  name="Chamara Silva",      age=33, gender="male",   specialization="cardio",   experience_years=8,  phone="0773456789", email="chamara@gym.com",  availability="evening", certification="NASM"),
            Trainer(id=6,  name="Dilani Fernando",    age=29, gender="female", specialization="yoga",     experience_years=4,  phone="0784567890", email="dilani@gym.com",   availability="fullday", certification="ACSM"),
            Trainer(id=7,  name="Kasun Rajapaksa",    age=31, gender="male",   specialization="strength", experience_years=6,  phone="0795678901", email="kasun@gym.com",    availability="morning", certification="ACE"),
            Trainer(id=8,  name="Sachini Madushani",  age=25, gender="female", specialization="crossfit", experience_years=1,  phone="0706789012", email="sachini@gym.com",  availability="evening", certification="NASM"),
            Trainer(id=9,  name="Nuwan Dissanayake",  age=38, gender="male",   specialization="cardio",   experience_years=10, phone="0717890123", email="nuwan@gym.com",    availability="fullday", certification="ACSM"),
            Trainer(id=10, name="Iresha Wickrama",    age=28, gender="female", specialization="yoga",     experience_years=3,  phone="0728901234", email="iresha@gym.com",   availability="morning", certification="ACE"),
        ]
        self.next_id = 11

    def get_all_trainers(self):
        return self.trainers

    def get_trainer_by_id(self, trainer_id: int):
        return next((t for t in self.trainers if t.id == trainer_id), None)

    def add_trainer(self, trainer_data):
        new_trainer = Trainer(id=self.next_id, **trainer_data.model_dump())
        self.trainers.append(new_trainer)
        self.next_id += 1
        return new_trainer

    def update_trainer(self, trainer_id: int, trainer_data):
        trainer = self.get_trainer_by_id(trainer_id)
        if trainer:
            update_data = trainer_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(trainer, key, value)
            return trainer
        return None

    def delete_trainer(self, trainer_id: int):
        trainer = self.get_trainer_by_id(trainer_id)
        if trainer:
            self.trainers.remove(trainer)
            return True
        return False