import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init(self):
        test = PlayerRepository()
        self.assertEqual(test.players, [])
        self.assertEqual(test.count, 0)

    def test_add(self):
        test = PlayerRepository()
        player = Advanced('test')
        test.add(player)

        self.assertEqual(test.players, [player])
        self.assertEqual(test.count, 1)

    def test_adding_a_already_existing_card(self):
        test = PlayerRepository()
        player = Advanced('test')
        test.add(player)

        with self.assertRaises(ValueError) as ex:
            test.add(player)

        self.assertEqual(str(ex.exception), "Player test already exists!")

    def test_remove(self):
        test = PlayerRepository()
        player = Advanced('test')
        test.add(player)
        test.remove('test')

        self.assertEqual(test.players, [])
        self.assertEqual(test.count, 0)

    def test_remove_empty_string(self):
        test = PlayerRepository()
        player = Advanced('test')
        test.add(player)

        with self.assertRaises(ValueError) as ex:
            test.remove('')

        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")

    def test_find(self):
        test = PlayerRepository()
        player = Advanced('test')
        test.add(player)

        self.assertEqual(test.find('test'), player)


if __name__ == '__main__':
    unittest.main()