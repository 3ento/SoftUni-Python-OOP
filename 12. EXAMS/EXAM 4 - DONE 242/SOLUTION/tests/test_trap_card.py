import unittest
from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_init(self):
        test = TrapCard("test")
        self.assertEqual(test.name, 'test')
        self.assertEqual(test.damage_points, 120)
        self.assertEqual(test.health_points, 5)

    def test_username_setter(self):
        with self.assertRaises(ValueError) as ex:
            test = TrapCard('')

        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")


if __name__ == '__main__':
    unittest.main()