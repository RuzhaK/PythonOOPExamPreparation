from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.laptop import Laptop

class YoungCouple(Room):
    room_cost = 20
    appliances=[TV(),TV(),Fridge(),Fridge(),Laptop(),Laptop()]

    def __init__(self,family_name: str, salary_one: float, salary_two:float):
        budget = salary_two+salary_one
        members_count = 2
        super().__init__(family_name,budget,members_count)
        expenses=self.appliances+self.children
        self.calculate_expenses(*expenses*30)


