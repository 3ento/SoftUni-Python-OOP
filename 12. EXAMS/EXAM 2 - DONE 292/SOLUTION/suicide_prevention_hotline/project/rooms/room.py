class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for el in args:
            for o in el:
                result += o.get_monthly_expense()

        self.expenses = result

    def __repr__(self):
        result = [f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]
        n = 1

        if len(self.children) > 0:
            for el in self.children:
                result.append(f"--- Child {n} monthly cost: {el.get_monthly_expense():.2f}$")
                n += 1

        if len(self.appliances) > 0:
            result.append(f"--- Appliances monthly cost: {sum([el.get_monthly_expense() for el in self.appliances]):.2f}$")

        return "\n".join(result)