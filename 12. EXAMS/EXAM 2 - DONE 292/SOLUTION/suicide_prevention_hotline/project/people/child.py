class Child:

    cost = 0

    def __init__(self, food_cost, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.cost * 30