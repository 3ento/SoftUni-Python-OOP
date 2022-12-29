import unittest

from project.controller import Controller


class TestController(unittest.TestCase):
    def test_add_player(self):
        test = Controller()
        player = test.add_player('Advanced', 'steve')

        self.assertEqual(test.player_repository.players, test.player_repository.players)
        self.assertEqual(test.player_repository.count, 1)
        self.assertEqual(str(test.add_player('Advanced', 'steve')), "Successfully added player of type Advanced with username: steve")

    def test_add_card(self):
        test = Controller()
        test.add_card('Magic', 'steve')

        self.assertEqual(test.card_repository.Cards, test.card_repository.Cards)
        self.assertEqual(test.card_repository.Count, 1)
        self.assertEqual(str(test.add_card('Magic', 'steve')), "Successfully added card of type MagicCard with name: steve")

    def test_add_player_card(self):
        test = Controller()
        test.add_player('Advanced', 'test')
        test.add_card('Magic', 'steve')

        temp = test.add_player_card('test', 'steve')
        self.assertEqual(temp, "Successfully added card: steve to user: test")

    def test_fight(self):
        test = Controller()
        test.add_player('Advanced', 'steve')
        test.add_player('Beginner', 'alex')
        a = test.fight('steve', 'alex')

        self.assertEqual(a, "Attack user health 250 - Enemy user health 90")

    def test_report(self):
        test = Controller()
        test.add_player('Advanced', 'steve')
        test.add_player('Beginner', 'alex')

        test.add_card('Magic', 'apple')
        test.add_card('Magic', 'pie')

        test.add_player_card('steve', 'apple')
        test.add_player_card('alex', 'pie')

        result = "Username: steve - Health: 250 - Cards 1\n" \
                 "### Card: apple - Damage: 5\n" \
                 "Username: alex - Health: 50 - Cards 1\n" \
                 "### Card: pie - Damage: 5"

        self.assertEqual(test.report(), result)


if __name__ == '__main__':
    unittest.main()