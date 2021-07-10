from RandomGenerator.randomDecimalSeeded import random_decimal_seeded


def random_number_decimal_seeded(start, end, seed):
    s = seed
    st = start
    e = end
    return random_decimal_seeded(st, e, s)
