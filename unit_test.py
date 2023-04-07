import unittest
import all_classes as main
import pandas as pd


class UnitTest(unittest.TestCase):
    def test_least_squares(self):
        twos = pd.DataFrame(2 for i in range(10))
        ones = pd.DataFrame(1 for i in range(10))
        database = main.Database()
        for i in range(10):
            self.assertEqual(database.find_least_squares(twos, ones).iloc[i, 0], 1)

    def test_sum_of_least_squares(self):
        twos = pd.DataFrame(2 for i in range(10))
        ones = pd.DataFrame(1 for i in range(10))
        database = main.Database()
        self.assertEqual(database.find_sum_of_least_squares(twos, ones), 10)

    def test_deviation(self):
        twos = pd.DataFrame(2 for i in range(10))
        ones = pd.DataFrame(1 for i in range(10))
        database = main.Database()
        for i in range(10):
            self.assertEqual(database.find_deviation(twos, ones).iloc[i, 0], 1)

    def test_any_deviation_greater_than_threshold(self):
        twos = pd.DataFrame(2 for i in range(10))
        ones = pd.DataFrame(1 for i in range(10))
        database = main.Database()
        self.assertTrue(database.any_deviation_greater_than_threshold(twos, ones, 0))
        self.assertFalse(database.any_deviation_greater_than_threshold(twos, ones, 2))


if __name__ == "__main__":
    unittest.main()
