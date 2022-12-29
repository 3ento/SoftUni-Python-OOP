import unittest
from project.factory.paint_factory import PaintFactory

class TestPaintFactory(unittest.TestCase):
    def test_init(self):
        obj = PaintFactory('test', 200)
        self.assertEqual(obj.name, 'test')
        self.assertEqual(obj.capacity, 200)
        self.assertEqual(obj.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient(self):
        obj = PaintFactory('test', 200)
        obj.add_ingredient('white', 10)
        self.assertEqual(obj.ingredients, {'white': 10})

    def test_remove_ingredient(self):
        obj = PaintFactory('test', 200)
        obj.add_ingredient('white', 10)
        obj.remove_ingredient('white', 5)
        self.assertEqual(obj.ingredients, {'white': 5})

    def test_add_ingredient_fail(self):
        obj = PaintFactory('test', 200)
        with self.assertRaises(TypeError) as ex:
            obj.add_ingredient('invalid', 10)

        self.assertEqual(str(ex.exception), "Ingredient of type invalid not allowed in PaintFactory")

    def test_remove_ingredient_fail(self):
        obj = PaintFactory('test', 200)
        with self.assertRaises(KeyError) as ex:
            obj.remove_ingredient("invalid", 10)

        self.assertEqual(ex.exception, KeyError('No such ingredient in the factory'))

    def test_repr(self):
        obj = PaintFactory('test', 200)
        obj.add_ingredient('white', 10)
        obj.add_ingredient('blue', 15)
        obj.add_ingredient('yellow', 15)
        result = "Factory name: test with capacity 200.\n" \
                 "white: 10\n" \
                 "blue: 15\n" \
                 "yellow: 15\n"
        self.assertEqual(repr(obj), result)


if __name__ == '__main__':
    unittest.main()

# 100/100
