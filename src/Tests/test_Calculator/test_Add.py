import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.test_data = CsvReader('data/addition.csv').data

    def tearDown(self):
        if CsvReader.data is not None:
            CsvReader.data = []

    def test_add_method_calculator(self):
        for row in self.test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
