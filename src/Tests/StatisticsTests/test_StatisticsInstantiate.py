import unittest
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        data = 'src/Tests/StatisticsTests/data/sample1.csv'
        self.statistics = Statistics(data)
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
