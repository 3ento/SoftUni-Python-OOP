from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    members = 2
    room_cost = 15

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, self.members)
        self.appliances = [TV(), Fridge(), Stove()] * self.members
        self.calculate_expenses(self.appliances)
