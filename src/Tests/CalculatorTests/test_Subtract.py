import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.csvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self):
        if CsvReader.data is not None:
            CsvReader.data = []

    def test_subtract_method_calculator(self):
        self.test_data = CsvReader('src/Tests/CalculatorTests/data/subtraction.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
