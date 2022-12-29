from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository

def player_str_to_obj(obj_name, list_of_objects):
    for el in list_of_objects:
        if obj_name == el.username:
            temp = el
            return temp

def card_str_to_obj(obj_name, list_of_objects):
    for el in list_of_objects:
        if obj_name == el.name:
            temp = el
            return temp

class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Advanced":
            player = Advanced(username)
        else:
            player = Beginner(username)

        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        if type == "Trap":
            card = TrapCard(name)
        else:
            card = MagicCard(name)

        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = player_str_to_obj(username, self.player_repository.players)
        card = card_str_to_obj(card_name, self.card_repository.Cards)

        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = player_str_to_obj(attack_name, self.player_repository.players)
        enemy = player_str_to_obj(enemy_name, self.player_repository.players)

        field = BattleField()
        field.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = []
        for el in self.player_repository.players:
            result.append(str(el))

        return "\n".join(result)