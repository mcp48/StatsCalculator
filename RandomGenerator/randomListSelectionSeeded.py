from numpy import random
from RandomGenerator.randomListSelection import random_list_selection


def random_list_selection_seeded(list, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        seeded_selection = random_list_selection(list)
        return seeded_selection
    finally:
        random.set_state(state)
