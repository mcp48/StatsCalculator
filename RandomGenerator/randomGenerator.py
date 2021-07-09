from RandomGenerator.randomDecimal import random_decimal
from RandomGenerator.randomDecimalList import random_decimal_list
from RandomGenerator.randomDecimalSeeded import random_decimal_seeded
from RandomGenerator.randomInteger import random_integer
from RandomGenerator.randomIntegerList import random_integer_list
from RandomGenerator.randomIntegerSeeded import random_integer_seeded


class Random:

    result = 0

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
