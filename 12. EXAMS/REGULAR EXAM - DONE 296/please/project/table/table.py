from abc import ABC, abstractmethod
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self._capacity = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people += number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for el in self.food_orders:
            bill += el.price
        for el in self.drink_orders:
            bill += el.price

        return bill

    def clear(self):
        self.drink_orders.clear()
        self.food_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        result = [f"Table: {self.table_number}", f"Type: {self.__class__.__name__}", f"Capacity: {self.capacity}"]

        if not self.is_reserved:
            return "\n".join(result)
