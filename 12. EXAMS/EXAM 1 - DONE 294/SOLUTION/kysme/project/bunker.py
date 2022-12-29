class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [el for el in self.supplies if el.__class__.__name__ == "FoodSupply"]
        if len(food_supplies) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [el for el in self.supplies if el.__class__.__name__ == "WaterSupply"]
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_supply = [el for el in self.medicine if el.__class__.__name__ == "Painkiller"]
        if len(painkillers_supply) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_supply

    @property
    def salves(self):
        salves_supply = [el for el in self.medicine if el.__class__.__name__ == "Salve"]
        if len(salves_supply) == 0:
            raise IndexError("There are no salves left!")
        return salves_supply


    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            if medicine_type == 'Painkiller':
                self.painkillers[-1].apply(survivor)
                self.painkillers.pop()
                return f"{survivor.name} healed successfully with {medicine_type}"

            self.salves[-1].apply(survivor)
            self.salves.pop()
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == 'FoodSupply':
                self.food[-1].apply(survivor)
                self.food.pop()
                return f"{survivor.name} sustained successfully with {sustenance_type}"

            self.water[-1].apply(survivor)
            self.water.pop()
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")