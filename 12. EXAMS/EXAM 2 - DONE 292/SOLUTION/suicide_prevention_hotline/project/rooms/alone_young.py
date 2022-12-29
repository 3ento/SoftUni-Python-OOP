from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    members = 1
    room_cost = 10

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, self.members)
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)