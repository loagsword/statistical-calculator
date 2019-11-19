import unittest
from src.Statistics.Statistics import Statistics
from src.CsvReader.csvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_p_value_calculator(self):
        self.statistics = Statistics()
        self.test_data = CsvReader('src/Tests/StatisticsTests/data/p_value.csv').data

        for row in self.test_data:
            self.assertEqual(self.statistics.p_value(row['EVENT'], row['SAMPLES']), float(row['RESULT']))
            self.assertEqual(self.statistics.result, float(row['RESULT']))


if __name__ == '__main__':
    unittest.main()
