from src.Calculator.Addition import addition as add
from src.Calculator.Division import division as divide


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = add(total, num)
    return divide(total, num_values)
