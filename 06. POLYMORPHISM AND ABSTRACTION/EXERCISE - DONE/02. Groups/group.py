class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self):
        result = []
        sep = ", "
        for el in self.people:
            result.append(repr(el))

        return f"Group {self.name} with members {sep.join(result)}"

    def __getitem__(self, item):
        return f"Person {item}: {repr(self.people[item])}"