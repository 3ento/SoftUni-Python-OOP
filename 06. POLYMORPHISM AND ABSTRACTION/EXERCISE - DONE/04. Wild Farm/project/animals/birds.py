from project.animals.animal import Bird

class Owl(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)
        self.acceptable_foods = ["Meat"]
        self.weight_gain = 0.25

    def make_sound(self):
        return f"Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)
        self.acceptable_foods = ["Meat", "Vegetable", "Fruit", "Seed"]
        self.weight_gain = 0.35

    def make_sound(self):
        return f"Cluck"
