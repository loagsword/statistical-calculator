import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.CsvReader import CsvReader
from decimal import Decimal


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self):
        if CsvReader.data is not None:
            CsvReader.data = []

    def test_divide_method_calculator(self):
        self.test_data = CsvReader('src/Tests/CalculatorTests/data/division.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertRaises(ZeroDivisionError, self.calculator.divide('0', row['Value 2']))


if __name__ == '__main__':
    unittest.main()
