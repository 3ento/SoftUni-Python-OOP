import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattlefield(unittest.TestCase):
    def test_fight_att_wins(self):
        field = BattleField()
        attacker = Advanced("winner")
        enemy = Beginner("lose")

        op_card = TrapCard('op')
        weak_card = MagicCard("weak")

        attacker.card_repository.Cards.append(op_card)
        attacker.card_repository.Cards.append(weak_card)

        enemy.card_repository.Cards.append(weak_card)

        field.fight(attacker, enemy)
        self.assertTrue(enemy.is_dead)

    def test_fight_one_player_dead(self):
        field = BattleField()
        attacker = Advanced("winner")
        enemy = Beginner("dead")

        enemy._health = 0

        with self.assertRaises(ValueError) as ex:
            field.fight(attacker, enemy)

        self.assertEqual(str(ex.exception), "Player is dead!")


if __name__ == '__main__':
    unittest.main()