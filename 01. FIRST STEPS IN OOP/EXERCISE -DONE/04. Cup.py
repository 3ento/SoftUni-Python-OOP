class Cup:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, milliliters):
        self.quantity += int(milliliters)
        if self.quantity > self.size:
            self.quantity -= int(milliliters)

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

# 100/100
