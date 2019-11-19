import unittest
from src.Statistics.Statistics import Statistics
from src.CsvReader.csvReader2 import csv_reader2


class MyTestCase(unittest.TestCase):

    def test_sample_std_deviation_calculator(self):
        self.statistics = Statistics()
        data = [1,2,3,4,1,6,8,23,34]
        result = 11.13552873
        self.assertEqual(self.statistics.sample_std_deviation(data), result)


if __name__ == '__main__':
    unittest.main()
