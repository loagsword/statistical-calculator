import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from decimal import Decimal


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()

