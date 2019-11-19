from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.Statistics.SampleMean import sample_mean
from src.Statistics.SampleStandardDeviation import sample_std_deviation


class Statistics(Calculator):
    result = 0

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def sample_mean(self, data, sample_size):
        self.result = sample_mean(data, sample_size)
        return self.result

    def sample_std_deviation(self, sample):
        self.result = sample_std_deviation(sample)
        return self.result
