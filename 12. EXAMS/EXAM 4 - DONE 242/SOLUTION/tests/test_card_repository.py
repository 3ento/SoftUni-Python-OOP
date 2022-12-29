import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_init(self):
        test = CardRepository()
        self.assertEqual(test.Cards, [])
        self.assertEqual(test.Count, 0)

    def test_add(self):
        test = CardRepository()
        card = MagicCard('test')
        test.add(card)

        self.assertEqual(test.Cards, [card])
        self.assertEqual(test.Count, 1)

    def test_adding_a_already_existing_card(self):
        test = CardRepository()
        card = MagicCard('test')
        test.add(card)

        with self.assertRaises(ValueError) as ex:
            test.add(card)

        self.assertEqual(str(ex.exception), "Card test already exists!")

    def test_remove(self):
        test = CardRepository()
        card = MagicCard('test')
        test.add(card)
        test.remove('test')

        self.assertEqual(test.Cards, [])
        self.assertEqual(test.Count, 0)

    def test_remove_empty_string(self):
        test = CardRepository()
        card = MagicCard('test')
        test.add(card)

        with self.assertRaises(ValueError) as ex:
            test.remove('')

        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_find(self):
        test = CardRepository()
        card = MagicCard('test')
        test.add(card)

        self.assertEqual(test.find('test'), card)


if __name__ == '__main__':
    unittest.main()