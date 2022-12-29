from project.subscription import Subscription
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.customer import Customer

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)
    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)
    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = []
        sub_obj = ''
        trainer_obj = ''
        plan_obj = ''

        for el in self.subscriptions:
            if el.id == subscription_id:
                sub_obj = el
                result.append(repr(el))
                break

        for el in self.customers:
            if el.id == sub_obj.customer_id:
                result.append(repr(el))
                break

        for el in self.trainers:
            if el.id == sub_obj.trainer_id:
                trainer_obj = el
                result.append(repr(trainer_obj))
                break

        for el in self.plans:
            if el.trainer_id == trainer_obj.id:
                plan_obj = el
                break

        for el in self.equipment:
            if el.id == plan_obj.equipment_id:
                result.append(repr(el))
                break

        result.append(repr(plan_obj))

        return "\n".join(result)

# 13/100
# 4/100
# 4/100
# 0/100
# 60/100
# 65/100
# 65/100
# 69/100
# 73/100
# 100/100
