from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for el in self.rooms:
            total_consumption += el.expenses + el.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        txt_res = []
        for el in self.rooms:
            total_cost = el.expenses + el.room_cost

            if el.budget >= total_cost:
                el.budget -= total_cost
                txt_res.append(f"{el.family_name} paid {(el.expenses+el.room_cost):.2f}$ and have {el.budget:.2f}$ left.")
            else:
                self.rooms.remove(el)
                txt_res.append(f"{el.family_name} does not have enough budget and must leave the hotel.")

        return "\n".join(txt_res)

    def status(self):
        result = [f"Total population: {sum([el.members_count for el in self.rooms])}"]
        for el in self.rooms:
            result.append(repr(el))

        return "\n".join(result)
