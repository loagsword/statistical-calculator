import unittest
from src.Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):

    def test_mean_calculator(self):
        self.test_data = 'src/Tests/StatisticsTests/data/sample1.csv'
        self.statistics = Statistics(self.test_data)
        for row in self.test_data:
            self.assertEqual(self.statistics.mean(), 3.5)
        print(self.test_data)


if __name__ == '__main__':
    unittest.main()
