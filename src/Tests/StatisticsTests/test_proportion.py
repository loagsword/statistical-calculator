import unittest
from src.Statistics.Statistics import Statistics
from src.CsvReader.csvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_proportion_calculator(self):
        self.statistics = Statistics()
        self.test_data = CsvReader('src/Tests/StatisticsTests/data/proportion.csv').data

        for row in self.test_data:
            self.assertEqual(self.statistics.get_proportion(row['SAMPLE SIZE'], row['OUTCOMES']), float(row['RESULT']))
            self.assertEqual(self.statistics.result, float(row['RESULT']))


if __name__ == '__main__':
    unittest.main()
