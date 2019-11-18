from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.Statistics.SampleMean import sample_mean
from src.CsvReader.csvReader import CsvReader
from src.CsvReader.csvReader2 import csv_reader2


class Statistics(Calculator):
    result = 0

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def sample_mean(self, data, sample_size):
        self.result = sample_mean(data, sample_size)
        return self.result
