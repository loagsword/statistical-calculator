from src.Statistics.Getsample import get_sample
from src.Statistics.Mean import mean
from src.Calculator.Square import square
from src.Calculator.SquareRoot import square_root


# Calculates the sample Standard deviation for a data in list format

def sample_std_deviation(sample):
    sample_mean = mean(sample)
    values_spread = [square(x - sample_mean) for x in sample]
    sample_sum = sum(values_spread)
    n = len(values_spread)
    std_mean = sample_sum / (n - 1)
    return round(square_root(std_mean), 9)

