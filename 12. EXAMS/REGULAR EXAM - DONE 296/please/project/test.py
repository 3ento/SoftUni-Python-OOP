from project.bakery import Bakery

bakery = Bakery("kill me")

print(bakery.add_food("Bread", "black", 1.5))
print(bakery.add_food("Bread", "white", 1))
print(bakery.add_food("Cake", "white", 1))

print(bakery.add_drink("Water", 'basic', 1, 'mine'))

print(bakery.add_table("InsideTable", 5, 50))
print(bakery.add_table("InsideTable", 1, 10))
print(bakery.add_table("OutsideTable", 55, 50))

print(bakery.reserve_table(10))

print(bakery.order_food(5, 'white'))
print(bakery.order_drink(5, 'basic'))


print(bakery.leave_table(5))

print(bakery.get_free_tables_info())

print(bakery.get_total_income())
