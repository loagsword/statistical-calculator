import unittest

from src.Statistics import Statistics

class StatisticsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def tearDown(self) -> None:
        if self.statistics is not None:
            self.statistics = None

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)
        self.assertEqual(self.statistics.data, [])

   # Testing mean
    def test_mean_method(self):
        data = [2, 2, 2, 4, 5]
        result = 3
        self.assertEqual(self.statistics.mean(data), result)
        self.assertEqual(self.statistics.data, result)

    # Testing mean
    def test_median_method(self):
            data = [2, 2, 2, 4, 5]
            result = 2
            self.assertEqual(self.statistics.median(data), result)
            self.assertEqual(self.statistics.data, result)

        if __name__ == '__main__':
         unittest.main()