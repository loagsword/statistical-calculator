from src.Calculator.Division import division


def get_proportion(sample_size, no_outcomes):
    sample_size = float(sample_size)
    no_outcomes = float(no_outcomes)
    return round(division(sample_size, no_outcomes), 3)
