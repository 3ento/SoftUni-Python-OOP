import unittest
from project.player.beginner import Beginner


class TestAdvanced(unittest.TestCase):
    def test_init(self):
        test = Beginner("test")
        self.assertEqual(test.username, 'test')
        self.assertEqual(test.health, 50)

    def test_username_setter(self):
        with self.assertRaises(ValueError) as ex:
            test = Beginner('')

        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")


if __name__ == '__main__':
    unittest.main()