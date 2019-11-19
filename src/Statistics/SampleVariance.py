from src.Statistics.SampleStandardDeviation import sample_std_deviation
from src.Calculator.Square import square


def sample_variance(sample):
    std_deviation = sample_std_deviation(sample)
    return square(std_deviation)
