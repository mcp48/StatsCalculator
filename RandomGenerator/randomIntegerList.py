from numpy import random


def random_integer_list(start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        integer_list = random.randint(start, end, length)
        return integer_list
    finally:
        random.set_state(state)
