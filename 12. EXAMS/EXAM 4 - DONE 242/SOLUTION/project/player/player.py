from abc import ABC, abstractmethod
from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError("Player's username cannot be an empty string.")
        self._username = value
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self._health = value

    @property
    def is_dead(self):
        return self._health <= 0

    def take_damage(self, damage_points):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self._health -= damage_points

    def __str__(self):
        sep = "\n"
        cards = []
        for el in self.card_repository.Cards:
            cards.append(f'### Card: {el.name} - Damage: {el.damage_points}')

        return f'Username: {self.username} - Health: {self.health} - Cards {self.card_repository.Count}\n' \
               f'{sep.join(cards)}'