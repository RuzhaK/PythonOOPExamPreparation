from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.stove import Stove

class OldCouple(Room):
    room_cost = 15
    appliances=[TV(), TV(),Fridge(),Fridge(),Stove(),Stove()]
    # todo for each person?
    def __init__(self,family_name: str, pension_one: float, pension_two:float):
        budget = pension_one+pension_two
        members_count = 2
        super().__init__(family_name,budget,members_count)
        self.calculate_expenses(*self.appliances)

