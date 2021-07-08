from numpy import random
from RandomGenerator.randomAmountSelection import random_amount_selection


def random_amount_selection_seeded(list, num_values, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        selection = random_amount_selection(list, num_values)
        return selection
    finally:
        random.set_state(state)
