class Room:
    family_name: str
    budget: float
    members_count: int
    children: list
    appliances=[]
    def __init__(self,name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget=budget
        self.members_count=members_count
        self.children=[]
        self.__expenses=0
        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value<0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses=value

    def calculate_expenses(self,*args):
        res=0
        for arg in args:

            res+=arg.cost
        self.expenses=res
# todo NOTE gore moje da niama vlojen cikal