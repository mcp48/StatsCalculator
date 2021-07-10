from RandomGenerator.randomIntegerSeeded import random_integer_seeded


def random_number_integer_seeded(start, end, seed):
    s = seed
    st = start
    e = end
    return random_integer_seeded(st, e, s)
