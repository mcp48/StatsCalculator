from numpy.random import uniform


def random_decimal(start, end):
    rand = uniform(start, end)
    # rounded to two decimal places
    rounded_decimal = round(rand, 2)
    return rounded_decimal
