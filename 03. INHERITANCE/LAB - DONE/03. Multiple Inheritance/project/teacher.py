from person import Person
from employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'


a = Teacher()
print(a.teach())
print(a.sleep())
print(a.get_fired())