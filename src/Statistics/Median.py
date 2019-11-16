def median(data):
    quotient, remainder = divmod(len(data), 2)
    if remainder:
        return sorted(data)[quotient]
    return float(sum(sorted(data)[quotient - 1:quotient + 1]) / 2)


