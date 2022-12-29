from project.appliances.appliance import Appliance


class Fridge(Appliance):

    fridge_cost = 1.2

    def __init__(self):
        super().__init__(self.fridge_cost)