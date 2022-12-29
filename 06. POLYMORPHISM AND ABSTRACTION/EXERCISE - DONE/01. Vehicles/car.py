from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        fuel_req = distance * (self.fuel_consumption + 0.9)
        if fuel_req <= self.fuel_quantity:
            self.fuel_quantity -= fuel_req