from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.CsvReader.CsvReader import CsvReader



class Statistics(Calculator):
    data = []

    def __init__(self):
        self.data = CsvReader('src/Tests/CalculatorTests/data/t_data.csv')
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result
