# Calculates the mean of a list
def mean(data_list):
    try:
        row = [float(x) for x in data_list]
        list_sum = sum(row)
        n = len(row)
        return round(list_sum / n, 2)
        # return round(divide(n, list_sum), 2)    # Also works, prone to raising errors

    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")


