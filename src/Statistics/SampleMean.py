from src.Statistics.Getsample import get_sample
from src.Statistics.Mean import mean


def sample_mean(data, sample_size):
    sample = get_sample(data, sample_size)
    try:
        return mean(sample)
        # row = [float(x) for x in sample]
        # list_sum = sum(row)
        # n = len(row)
        # return round(list_sum / n, 2)
        # # return round(divide(n, list_sum_sum), 2)    # Also works, prone to raising errors

    except ZeroDivisionError:
        print("Zero Division Error: Sample size must be greater than 0")
    except TypeError:
        print("Type Error: Check your data inputs.")

    # check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    # https://realpython.com/python-exceptions/
    # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
