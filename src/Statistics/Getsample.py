import random


def get_sample(data, sample_size):
    try:
        random_values = random.sample(data, k=sample_size)
        return random_values
    except ValueError:
        print("Value Error: Check your data inputs. "
              "Sample is larger than population or may be negative")
