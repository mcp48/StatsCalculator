from numpy import random


def random_decimal_list(start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        decimal_list = random.uniform(start, end, length)
        return decimal_list
    finally:
        random.set_state(state)
