from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten
        self.acceptable_foods = None
        self.weight_gain = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if type(food).__name__ not in self.acceptable_foods:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += self.weight_gain * food.quantity



class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"



class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

# 100/100
