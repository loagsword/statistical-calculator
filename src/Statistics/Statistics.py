from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean
from src.Statistics.SampleMean import sample_mean
from src.Statistics.SampleStandardDeviation import sample_std_deviation
from src.Statistics.Proportion import get_proportion
from src.Statistics.SampleVariance import sample_variance


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

    def get_proportion(self, sample_size, no_outcomes):
        self.result = get_proportion(sample_size, no_outcomes)
        return self.result

    def sample_variance(self, sample):
        self.result = sample_variance(sample)
        return self.result
