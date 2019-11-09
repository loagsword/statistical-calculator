import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self):
        if CsvReader.data is not None:
            CsvReader.data = []

    def test_results_property_calculator(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()