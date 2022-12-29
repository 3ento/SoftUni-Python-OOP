from project.dvd import DVD
from project.customer import Customer

class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer_obj = ''
        dvd_obj = ''

        for el in self.dvds:
            if el.id == dvd_id:
                dvd_obj = el
                break
        for el in self.customers:
            if el.id == customer_id:
                customer_obj = el
                break

        for el in customer_obj.rented_dvds:
            if el.id == dvd_id:
                return f"{customer_obj.name} has already rented {dvd_obj.name}"
        if dvd_obj.is_rented:
            return "DVD is already rented"
        if dvd_obj.age_restriction > customer_obj.age:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} to rent this movie"

        dvd_obj.is_rented = True
        customer_obj.rented_dvds.append(dvd_obj)
        return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_obj = ''
        dvd_obj = ''

        for el in self.dvds:
            if el.id == dvd_id:
                dvd_obj = el
        for el in self.customers:
            if el.id == customer_id:
                customer_obj = el

        if dvd_obj in customer_obj.rented_dvds:
            customer_obj.rented_dvds.remove(dvd_obj)
            dvd_obj.is_rented = False
            return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
        return f"{customer_obj.name} does not have that DVD"

    def __repr__(self):
        result = []
        for el in self.customers:
            result.append(repr(el))
        for el in self.dvds:
            result.append(repr(el))
        return "\n".join(result)