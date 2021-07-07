from project.rooms.room import Room

class Everland:
    rooms:list

    def __init__(self):
        self.rooms=[]

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption=0
        for r in self.rooms:
            total_consumption+=r.expenses+r.room_cost

        return f"Monthly consumption: {total_consumption:0.2f}$."

    def pay(self):
        strings=[]
        rooms_to_remove=[]
        for room in self.rooms:

            monthly_expenses=(room.expenses+room.room_cost)

            if room.budget>=monthly_expenses:

                strings.append(f"{room.family_name} paid {monthly_expenses:0.2f}$ and have {room.budget}$ left.")
                room.budget -= monthly_expenses
            else:

                strings.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)
        for room in rooms_to_remove:
            self.rooms.pop(self.rooms.index(room))

        return '\n'.join(strings)

    def status(self):
        s=''
        all_people_in_the_hotel=sum([room.members_count for room in self.rooms])
        s+=f"Total population: {all_people_in_the_hotel}\n"
        for room in self.rooms:

            room_name=room.family_name
            members=room.members_count
            current_budget=room.budget
            expenses=room.expenses
            s+=f"{room_name} with {members} members. Budget: {current_budget:0.2f}$, Expenses: {expenses:0.2f}$\n"
            for n,child in enumerate(room.children,1):
                cost_for_one_month=child.cost*30
                s+=f"--- Child {n} monthly cost: {cost_for_one_month:.2f}$\n"
            cost_of_all_appliances=sum([a.cost for a in room.appliances])

            s+=f"--- Appliances monthly cost: {cost_of_all_appliances*30:0.2f}$\n"
        return s


