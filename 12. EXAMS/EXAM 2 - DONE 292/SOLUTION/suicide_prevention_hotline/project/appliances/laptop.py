from project.appliances.appliance import Appliance


class Laptop(Appliance):
    laptop_cost = 1

    def __init__(self):
        super().__init__(self.laptop_cost)