import unittest
from src.Statistics.Statistics import Statistics
from src.CsvReader.csvReader2 import csv_reader2
from src.Statistics.Getsample import get_sample


class MyTestCase(unittest.TestCase):

    def test_sample_mean_calculator(self):
        self.statistics = Statistics()
        self.test_data = csv_reader2('src/Tests/StatisticsTests/data/mean.csv')

        for row in self.test_data:
            # check that get sample returns the proper number of samples
            self.assertEqual(len(get_sample(row, 3)), 3)

            # check that sample size is not 0
            self.assertRaises(ZeroDivisionError, self.statistics.sample_mean([], 0))

        #   Test sample is not larger than population
        self.assertRaises(ValueError, self.statistics.sample_mean([1, 2, 3], 4))


if __name__ == '__main__':
    unittest.main()
