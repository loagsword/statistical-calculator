import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader
from decimal import Decimal

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self):
        if CsvReader.data is not None:
            CsvReader.data = []

    def test_square_method_calculator(self):
        self.test_data = CsvReader('src/td/square.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
