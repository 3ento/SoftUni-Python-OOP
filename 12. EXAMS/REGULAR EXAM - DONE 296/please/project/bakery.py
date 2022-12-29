from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        already_existis = any([name == el.name and food_type == el.__class__.__name__ for el in self.food_menu])
        if already_existis:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Cake":
            cake = Cake(name, price)
            self.food_menu.append(cake)
            return f"Added {name} ({food_type}) to the food menu"
        else:
            bread = Bread(name, price)
            self.food_menu.append(bread)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        already_existis = any([name == el.name and drink_type == el.__class__.__name__ for el in self.drinks_menu])
        if already_existis:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            tea = Tea(name, portion, brand)
            self.drinks_menu.append(tea)
            return f"Added {name} ({brand}) to the drink menu"
        else:
            water = Water(name, portion, brand)
            self.drinks_menu.append(water)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        already_existis = any([table_number == el.table_number and table_type == el.__class__.__name__ for el in self.tables_repository])
        if already_existis:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == 'InsideTable':
            it = InsideTable(table_number, capacity)
            self.tables_repository.append(it)
            return f"Added table number {table_number} in the bakery"
        else:
            ot = OutsideTable(table_number, capacity)
            self.tables_repository.append(ot)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        tables_available = [el for el in self.tables_repository if not el.is_reserved if el.capacity >= number_of_people]
        if not tables_available:
            return f"No available table for {number_of_people} people"

        tables_available[0].reserve(number_of_people)
        return f"Table {tables_available[0].table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = [el for el in self.tables_repository if el.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"

        food_not_in_menu = []
        food_in_menu = []
        for el in args:  # food names
            for food_obj in self.food_menu:  # iterating through the food objects
                if el == food_obj.name:
                    el = food_obj
                    table[0].order_food(el)
                    food_in_menu.append(el)
                    break
            if el not in food_in_menu:
                food_not_in_menu.append(el)

        result = [f"Table {table_number} ordered:"]
        for el in food_in_menu:
            result.append(repr(el))
        if food_not_in_menu:
            result.append(f"{self.name} does not have in the menu:")
            for el in food_not_in_menu:
                result.append(el)

        return "\n".join(result)

    def order_drink(self, table_number, *args):
        table = [el for el in self.tables_repository if el.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"

        drink_not_in_menu = []
        drink_in_menu = []
        for el in args:
            for drink_obj in self.drinks_menu:
                if el == drink_obj.name:
                    el = drink_obj
                    table[0].order_drink(el)
                    drink_in_menu.append(el)
                    break

            if el not in drink_in_menu:
                drink_not_in_menu.append(el)

        result = [f"Table {table_number} ordered:"]
        for el in drink_in_menu:
            result.append(repr(el))
        if drink_not_in_menu:
            result.append(f"{self.name} does not have in the menu:")
            for el in drink_not_in_menu:
                result.append(el)

        return "\n".join(result)

    def leave_table(self, table_number):
        table = [el for el in self.tables_repository if el.table_number == table_number]
        self.total_income += table[0].get_bill()

        result = f"Table: {table_number}\n" \
                 f"Bill: {f'{table[0].get_bill():.2f}'}"
        table[0].clear()

        return result

    def get_free_tables_info(self):
        result = []
        for el in self.tables_repository:
            if not el.is_reserved:
                result.append(el.free_table_info())
                # result.append("\n")

        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
