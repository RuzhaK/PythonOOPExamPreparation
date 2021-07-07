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
        self.expenses=0
    #     todo ako imame setter, nikade drugade ne slagame dwe dolni cherti izwan tiah!!!None da e che ne e kazano che e 0, ама после валидейшъна как?

        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value and value<0 :
            raise ValueError("Expenses cannot be negative")
        self.__expenses=value

    def calculate_expenses(self,*args):
        res=0
        for arg in args:

            res+=arg.get_monthly_expense()
        self.expenses=res

