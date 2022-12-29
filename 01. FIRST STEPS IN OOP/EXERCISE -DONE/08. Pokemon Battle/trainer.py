from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon.name)
        return f"Caught {Pokemon.pokemon_details(pokemon)}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == self.pokemons:
                self.pokemons.remove(pokemon_name)
                return f"You have released {pokemon_name}"
        return 'Pokemon is not caught'


    def trainer_data(self):
        result = ""
        result += f'Pokemon Trainer {self.name}\n'
        result += f"Pokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            result += "- " + p.pokemon_details()


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

# fuck this, the code works, the module bullshit doesn't
