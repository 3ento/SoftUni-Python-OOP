from project.appliances.appliance import Appliance


class TV(Appliance):
    tv_cost = 1.5

    def __init__(self):
        super().__init__(self.tv_cost)