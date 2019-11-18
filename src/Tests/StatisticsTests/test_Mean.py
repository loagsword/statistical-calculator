import unittest
from src.Statistics.Statistics import Statistics
from src.CsvReader.csvReader2 import csv_reader2


class MyTestCase(unittest.TestCase):

    def test_mean_calculator(self):
        self.statistics = Statistics()
        self.test_data = csv_reader2('src/Tests/StatisticsTests/data/mean.csv')
        result = 3
        for row in self.test_data:
            self.assertEqual(self.statistics.mean(row), result)


if __name__ == '__main__':
    unittest.main()
