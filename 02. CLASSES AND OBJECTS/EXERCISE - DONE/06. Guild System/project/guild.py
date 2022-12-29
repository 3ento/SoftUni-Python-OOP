from player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        if player.guild != "Unaffiliated" and player.guild != self.name:
            return "Player {player_name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        player.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        player_obj = ''
        for el in self.players:
            if player_name == el.name:
                player_obj = el

        if player_obj == '':
            return f"Player {player_name} is not in the guild."

        self.players.remove(player_obj)
        player_obj.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = ""
        for el in self.players:
            result += el.player_info()
        return f"Guild: {self.name}\n{result}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Kill", 200))
print(player.player_info())

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(player))
print(guild.kick_player("George"))
print(guild.assign_player(player))

guild_two = Guild("The Pact")

player_two = Player("HeaveN", 100, 10)
print(player_two.add_skill("Building", 10))
print(player_two.add_skill("UHC", 10))
print(guild_two.assign_player(player_two))

# 72/100
# 81/100
# 90/100
# 90/100
# 90/100
# 90/100
# fuck it