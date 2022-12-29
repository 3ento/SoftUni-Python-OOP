from animal import Animal

class Dog(Animal):
    def bark(self):
        return 'barking...'


rex = Dog()
print(rex.bark())
print(rex.eat())