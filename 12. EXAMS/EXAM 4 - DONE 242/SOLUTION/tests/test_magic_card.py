import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_init(self):
        test = MagicCard("test")
        self.assertEqual(test.name, 'test')
        self.assertEqual(test.damage_points, 5)
        self.assertEqual(test.health_points, 80)

    def test_username_setter(self):
        with self.assertRaises(ValueError) as ex:
            test = MagicCard('')

        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")


if __name__ == '__main__':
    unittest.main()