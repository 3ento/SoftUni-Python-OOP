from car import Car

class SportsCar(Car):
    @staticmethod
    def race():
        return 'racing...'


smth = SportsCar()
print(smth.move())
print(smth.drive())
print(smth.race())