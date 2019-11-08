from decimal import Decimal

def division(a, b):
    if int(a) != 0:
        return round((Decimal(b) / Decimal(a)), 9)
    else:
        return 'error, the divisor can not be zero'