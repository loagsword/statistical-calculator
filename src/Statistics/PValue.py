from src.Calculator.Division import division


def p_value(event_occurrence, sample_size):
    event = float(event_occurrence)
    sample_size = float(sample_size)
    return round(division(sample_size, event), 3)
