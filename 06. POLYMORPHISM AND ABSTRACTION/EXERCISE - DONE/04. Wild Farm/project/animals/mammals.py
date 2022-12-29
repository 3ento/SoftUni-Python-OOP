from project.animals.animal import Mammal

class Mouse(Mammal):

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)
        self.acceptable_foods = ["Vegetable", "Fruit"]
        self.weight_gain = 0.10

    def make_sound(self):
        return f"Squeak"


class Dog(Mammal):

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)
        self.acceptable_foods = ["Meat"]
        self.weight_gain = 0.40

    def make_sound(self):
        return f"Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)
        self.acceptable_foods = ["Vegetable", "Meat"]
        self.weight_gain = 0.30

    def make_sound(self):
        return f"Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)
        self.acceptable_foods = ["Meat"]
        self.weight_gain = 1

    def make_sound(self):
        return f"ROAR!!!"
