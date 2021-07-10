from AdditionalModules.GeneratorFiles.randomNumberDecimal import random_number_decimal
from AdditionalModules.GeneratorFiles.randomNumberDecimalSeeded import random_number_decimal_seeded
from AdditionalModules.GeneratorFiles.randomNumberInteger import random_number_integer
from AdditionalModules.GeneratorFiles.randomNumberIntegerSeeded import random_number_integer_seeded
from RandomGenerator.randomGenerator import Random


class RandomNumberGenerator(Random):

    result = 0

    def random_number_generator_integer(self, start, end):
        self.result = random_number_integer(start, end)
        return self.result

    def random_number_generator_integer_seeded(self, start, end, seed):
        self.result = random_number_integer_seeded(start, end, seed)
        return self.result

    def random_number_generator_decimal(self, start, end):
        self.result = random_number_decimal(start, end)
        return self.result

    def random_number_generator_decimal_seeded(self, start, end, seed):
        self.result = random_number_decimal_seeded(start, end, seed)
        return self.result
