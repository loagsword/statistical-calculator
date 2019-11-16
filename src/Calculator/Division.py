from decimal import Decimal


def division(a, b):
    # if int(a) != 0:
    #     return round((Decimal(b) / Decimal(a)), 9)
    # else:
    #     return 'error, the divisor can not be zero'

    try:
        return round((float(b) / float(a)), 9)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")
