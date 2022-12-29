import unittest
from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def test_init(self):
        test = Advanced("test")
        self.assertEqual(test.username, 'test')
        self.assertEqual(test.health, 250)

    def test_username_setter(self):
        with self.assertRaises(ValueError) as ex:
            test = Advanced('')

        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")


if __name__ == '__main__':
    unittest.main()