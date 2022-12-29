from project.player.player import Player

def str_to_obj(obj_name, list_of_objects):
    for el in list_of_objects:
        if obj_name == el.username:
            temp = el
            return temp

class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        temp = str_to_obj(player, self.players)

        if player == '':
            raise ValueError("Player cannot be an empty string!")

        self.players.remove(temp)
        self.count -= 1

    def find(self, username: str):
        player = str_to_obj(username, self.players)
        return player

