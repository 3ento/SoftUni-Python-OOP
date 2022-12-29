# from project.customer import Customer
# from project.dvd import DVD
# from project.movie_world import MovieWorld
#
# import unittest
#
#
# class TestsMovieWorld(unittest.TestCase):
#
#     def test_dvd_class_method(self):
#         dvd = DVD.from_date(1, "A", "16.10.1997", 18)
#         self.assertEqual(dvd.name, "A")
#         self.assertEqual(dvd.id, 1)
#         self.assertEqual(dvd.creation_month, "October")
#         self.assertEqual(dvd.creation_year, 1997)
#         self.assertEqual(dvd.age_restriction, 18)
#         self.assertEqual(dvd.is_rented, False)
#
#     def test_movie_world_return_dvd_success(self):
#         movie_world = MovieWorld("Test")
#         d = DVD("A", 1, 1254, "February", 10)
#         c = Customer("Pesho", 20, 4)
#         movie_world.add_customer(c)
#         movie_world.add_dvd(d)
#         movie_world.rent_dvd(4, 1)
#         result = movie_world.return_dvd(4, 1)
#         self.assertEqual(result, "Pesho has successfully returned A")
#         self.assertEqual(c.rented_dvds, [])
#         self.assertEqual(d.is_rented, False)
#
#
#
# if __name__ == "__main__":
#     unittest.main()