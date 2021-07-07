from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.laptop import Laptop
from ..people.child import Child

class YoungCoupleWithChildren(Room):
    default_room_cost = 30
    children=[]
    appliances=[]

    def __init__(self,family_name: str, salary_one: float, salary_two:float,*children:Child):
        budget = salary_two+salary_one
        members_count = 2+len(children)
        super().__init__(family_name, budget, members_count)
        self.room_cost = self.default_room_cost
        self.children=list(children)
        for _ in range(members_count):
            self.appliances.append(Laptop())
            self.appliances.append(Fridge())
            self.appliances.append(TV())

        expenses=self.appliances+self.children
        self.calculate_expenses(*expenses)


