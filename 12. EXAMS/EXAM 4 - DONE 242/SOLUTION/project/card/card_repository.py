def str_to_obj(obj_name, list_of_objects):
    for el in list_of_objects:
        if obj_name == el.name:
            temp = el
            return temp

class CardRepository:
    def __init__(self):
        self.Count = 0
        self.Cards = []

    def add(self, card):
        if card in self.Cards:
            raise ValueError(f"Card {card.name} already exists!")

        self.Cards.append(card)
        self.Count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")

        self.Cards.remove(str_to_obj(card, self.Cards))
        self.Count -= 1

    def find(self, name):
        return str_to_obj(name, self.Cards)