import unittest
from pprint import pprint
from RandomGenerator.randomGenerator import Random


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = Random()
        self.start = 1
        self.end = 100
        self.length = 6
        self.seed = 8
        self.num_val = 3
        self.list = self.random.random_integer_list(self.start, self.end, self.length, self.seed)

    def test_instantiate_calculator_self(self):
        self.assertIsInstance(self.random, Random)

    def test_random_integer(self):
        int_random = str(self.random.random_integer(self.start, self.end))
        pprint("Random integer: " + int_random)
        self.assertEqual(isinstance(self.random.random_integer(self.start, self.end), int), True)

    def test_random_integer_seeded(self):
        int_seeded = str(self.random.random_integer_seeded(self.start, self.end, self.seed))
        pprint("Random seeded integer: " + int_seeded)
        self.assertEqual(int_seeded, str(self.random.random_integer_seeded(self.start, self.end, self.seed)))

    def test_random_decimal(self):
        decimal_random = str(self.random.random_decimal(self.start, self.end))
        pprint("Random decimal: " + decimal_random)
        self.assertEqual(isinstance(self.random.random_decimal(self.start, self.end), float), True)

    def test_random_decimal_seeded(self):
        seeded_decimal = str(self.random.random_decimal_seeded(self.start, self.end, self.seed))
        pprint("Seeded decimal: " + seeded_decimal)
        self.assertEqual(seeded_decimal, str(self.random.random_decimal_seeded(self.start, self.end, self.seed)))

    def test_random_integer_list(self):
        integer_array = str(self.random.random_integer_list(self.start, self.end, self.length, self.seed))
        integer_list = (self.random.random_integer_list(self.start, self.end, self.length, self.seed))
        pprint("Integer array with a seed: " + integer_array)
        for val in integer_list:
            test_value = int(val)
            self.assertEqual(isinstance(test_value, int), True)

    def test_random_decimal_list(self):
        decimal_array = str(self.random.random_decimal_list(self.start, self.end, self.length, self.seed))
        decimal_list = (self.random.random_decimal_list(self.start, self.end, self.length, self.seed))
        pprint("Decimal array with a seed: " + decimal_array)
        for val in decimal_list:
            test_value = float(val)
            self.assertEqual(isinstance(test_value, float), True)


if __name__ == '__main__':
    unittest.main()
