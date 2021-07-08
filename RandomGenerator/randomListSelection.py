from numpy import random


def random_list_selection(list):
    try:
        random_selection = random.choice(list)
        return random_selection
    except ValueError as error:
        error = "ERROR!  That is an empty array.  Try again."
        return error
