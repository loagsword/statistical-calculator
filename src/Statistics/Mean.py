from src.Calculator.Addition import addition as add
from src.Calculator.Division import division as divide


def mean(data):
    data = []
    try:
        mean_floats = [float(i) for i in data]
        num_values = len(mean_floats)
        total = 0
        for num in mean_floats:
            total = add(total, num)
        return divide(total, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
