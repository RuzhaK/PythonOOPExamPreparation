from .room import Room
from project.appliances.tv import TV

class AloneYoung(Room):
    default_room_cost = 10
    appliances=[TV()]

    def __init__(self,family_name: str, salary: float):
        budget = salary
        members_count = 1
        super().__init__(family_name,budget,members_count)
        self.room_cost = self.default_room_cost
        self.calculate_expenses(*self.appliances*30)





