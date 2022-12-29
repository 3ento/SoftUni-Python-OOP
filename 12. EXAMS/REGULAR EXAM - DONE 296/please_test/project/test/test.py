from pet_shop import PetShop
import unittest


class Test(unittest.TestCase):
    def test_init(self):
        test = PetShop("test")
        self.assertEqual(test.name, 'test')
        self.assertEqual(test.food, {})
        self.assertEqual(test.pets, [])

    def test_add_food(self):
        test = PetShop("test")
        test.add_food('dry', 1000)
        self.assertEqual(test.food, {'dry': 1000})
        self.assertEqual(str(test.add_food('dry', 1000)), "Successfully added 1000.00 grams of dry.")

    def test_add_food_fail(self):
        test = PetShop("test")
        with self.assertRaises(ValueError) as ex:
            test.add_food('dry', 0)

        self.assertEqual(str(ex.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_existing_food(self):
        test = PetShop("test")
        test.add_food('dry', 1000)
        test.add_food('dry', 1000)
        self.assertEqual(test.food, {'dry': 2000})

    def test_add_pet(self):
        test = PetShop("test")
        self.assertEqual(str(test.add_pet("Aya")),f"Successfully added Aya.")
        self.assertEqual(test.pets, ['Aya'])

    def test_add_existing_pet(self):
        test = PetShop("test")
        test.add_pet('Aya')
        with self.assertRaises(Exception) as ex:
            test.add_pet('Aya')

        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_feed_pet(self):
        test = PetShop("test")
        test.add_food('dry', 1000)
        test.add_pet('Aya')
        test.feed_pet('dry', 'Aya')
        self.assertEqual(test.food, {'dry': 900})
        self.assertEqual(test.feed_pet('dry', 'Aya'), "Aya was successfully fed")

    def test_feed_pet_that_doesnt_exist(self):
        test = PetShop("test")
        test.add_food('dry', 1000)
        with self.assertRaises(Exception) as ex:
            test.feed_pet('dry', 'Aya')

        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_pet_with_no_food(self):
        test = PetShop('test')
        test.add_pet('Aya')
        self.assertEqual(test.feed_pet('dry', 'Aya'), 'You do not have dry')

    def test_feed_pet_with_less_than_100_food(self):
        test = PetShop("test")
        test.add_food('dry', 99)
        test.add_pet('Aya')
        self.assertEqual(test.feed_pet('dry', 'Aya'), "Adding food...")
        self.assertEqual(test.food, {'dry': 1099.00})

    def test_repr(self):
        test = PetShop("test")
        test.add_pet('Aya')
        test.add_pet('Lucky')
        self.assertEqual(repr(test), "Shop test:\nPets: Aya, Lucky")


if __name__ == '__main__':
    unittest.main()
