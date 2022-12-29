import unittest
from tests.project.room import Room
from tests.project.room import Child


class TestRoom(unittest.TestCase):
    def test_init(self):
        test = Room("test", 100, 2)
        self.assertEqual(test.family_name, "test")
        self.assertEqual(test.budget, 100)
        self.assertEqual(test.members_count, 2)
        self.assertEqual(test.children, [])
        self.assertEqual(test.expenses, 0)

    def test_expenses(self):
        test = Room("test", 100, 2)
        test.expenses = 10
        self.assertEqual(test._expenses, 10)

    def test_expenses_fail(self):
        test = Room("test", 100, 2)
        with self.assertRaises(ValueError) as ex:
            test.expenses = -10

        self.assertEqual(str(ex.exception), "Expenses cannot be negative")

    def test_calculate_expenses(self):
        test = Room("test", 100, 2)
        c1 = Child(20, 10, 10)
        test.calculate_expenses([c1])
        self.assertEqual(test._expenses, 1200)

if __name__ == '__main__':
    unittest.main()
