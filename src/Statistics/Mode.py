from collections import Counter

def get_mode(num_list):
    counter = Counter(num_list)
    if len(counter) > 1:  # ensure at least 2 unique elements
        possible_mode, next_highest = counter.most_common(2)
        if possible_mode[1] > next_highest[1]:
            return possible_mode[0]
    return "No mode"