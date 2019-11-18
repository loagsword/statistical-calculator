import unittest
from src.Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.statistics = Statistics()
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
