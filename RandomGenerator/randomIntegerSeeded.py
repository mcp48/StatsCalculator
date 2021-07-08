from numpy import random
from RandomGenerator.randomInteger import random_integer


def random_integer_seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        rand_integer_seeded = random_integer(start, end)
        return rand_integer_seeded
    finally:
        random.set_state(state)
