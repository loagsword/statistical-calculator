import unittest
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def test_sample_std_deviation_calculator(self):
        self.statistics = Statistics()
        data = [12, 13, 45, 56, 55, 54, 23]
        result = 361
        self.assertEqual(self.statistics.sample_variance(data), result)


if __name__ == '__main__':
    unittest.main()
