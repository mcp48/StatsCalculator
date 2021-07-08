from RandomGenerator.randomAmountSelection import random_amount_selection
from RandomGenerator.randomAmountSelectionSeeded import random_amount_selection_seeded
from RandomGenerator.randomDecimal import random_decimal
from RandomGenerator.randomDecimalList import random_decimal_list
from RandomGenerator.randomDecimalSeeded import random_decimal_seeded
from RandomGenerator.randomInteger import random_integer
from RandomGenerator.randomIntegerList import random_integer_list
from RandomGenerator.randomIntegerSeeded import random_integer_seeded
from RandomGenerator.randomListSelection import random_list_selection
from RandomGenerator.randomListSelectionSeeded import random_list_selection_seeded


class Random:

    result = 0

    def random_amount_selection(self, list, num_values):
        self.result = random_amount_selection(list, num_values)
        return self.result

    def random_amount_selection_seeded(self, list, num_values, seed):
        self.result = random_amount_selection_seeded(list, num_values, seed)
        return self.result

    def random_decimal(self, start, end):
        self.result = random_decimal(start, end)
        return self.result

    def random_decimal_seeded(self, start, end, seed):
        self.result = random_decimal_seeded(start, end, seed)
        return self.result

    def random_decimal_list(self, start, end, length, seed):
        self.result = random_decimal_list(start, end, length, seed)
        return self.result

    def random_integer(self, start, end):
        self.result = random_integer(start, end)
        return self.result

    def random_integer_seeded(self, start, end, seed):
        self.result = random_integer_seeded(start, end, seed)
        return self.result

    def random_integer_list(self, start, end, length, seed):
        self.result = random_integer_list(start, end, length, seed)
        return self.result

    def random_list_selection(self, list):
        self.result = random_list_selection(list)
        return self.result

    def random_list_selection_seeded(self, list, seed):
        self.result = random_list_selection_seeded(list, seed)
        return self.result
