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

    def test_random_integer_method(self):
        int_random = str(self.random.random_integer(self.start, self.end))
        pprint("Random integer: " + int_random)
        self.assertEqual(isinstance(self.random.random_integer(self.start, self.end), int), True)


if __name__ == '__main__':
    unittest.main()
