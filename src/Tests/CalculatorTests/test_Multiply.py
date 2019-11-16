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

    def test_multiply_method_calculator(self):
        self.test_data = CsvReader('src/Tests/CalculatorTests/data/multiplication.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()