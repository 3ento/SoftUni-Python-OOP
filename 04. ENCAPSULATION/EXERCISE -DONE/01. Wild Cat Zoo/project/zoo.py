class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        # self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            # self.__workers_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for el in self.workers:
            if el.name == worker_name:
                self.workers.remove(el)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for el in self.workers:
            salaries += el.salary

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        cost = 0
        for el in self.animals:
            cost += el.money_for_care

        if self.__budget >= cost:
            self.__budget -= cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion_count, lion_stats = 0, []
        tiger_count, tiger_stats = 0, []
        cheetah_count, cheetah_stats = 0, []

        for el in self.animals:
            if el.__class__.__name__ == "Lion":
                lion_count += 1
                lion_stats.append(repr(el))
            elif el.__class__.__name__ == "Tiger":
                tiger_count += 1
                tiger_stats.append(repr(el))
            elif el.__class__.__name__ == "Cheetah":
                cheetah_count += 1
                cheetah_stats.append(repr(el))

        result = []
        if lion_count > 0:
            result.append(f"----- {lion_count} Lions:")
            for el in lion_stats:
                result.append(el)
        if tiger_count > 0:
            result.append(f"----- {tiger_count} Tigers:")
            for el in tiger_stats:
                result.append(el)

        if cheetah_count > 0:
            result.append(f"----- {cheetah_count} Cheetahs:")
            for el in cheetah_stats:
                result.append(el)

        return f"You have {len(self.animals)} animals\n" + "\n".join(result)

    def workers_status(self):
        keeper_count, keeper_stats = 0, []
        caretaker_count, caretaker_stats = 0, []
        vet_count, vet_stats = 0, []

        for el in self.workers:
            if el.__class__.__name__ == "Keeper":
                keeper_count += 1
                keeper_stats.append(repr(el))
            elif el.__class__.__name__ == "Caretaker":
                caretaker_count += 1
                caretaker_stats.append(repr(el))
            elif el.__class__.__name__ == "Vet":
                vet_count += 1
                vet_stats.append(repr(el))

        result = []
        if keeper_count > 0:
            result.append(f"----- {keeper_count} Keepers:")
            for el in keeper_stats:
                result.append(el)
        if caretaker_count > 0:
            result.append(f"----- {caretaker_count} Caretakers:")
            for el in caretaker_stats:
                result.append(el)

        if vet_count > 0:
            result.append(f"----- {vet_count} Vets:")
            for el in vet_stats:
                result.append(el)

        return f"You have {len(self.workers)} workers\n" + "\n".join(result)
