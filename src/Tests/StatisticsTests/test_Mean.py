import unittest
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        data = 'src/Tests/StatisticsTests/data/sample1.csv'
        self.statistics = Statistics(data)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
