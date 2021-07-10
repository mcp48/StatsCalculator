import unittest
from AdditionalModules.type_checker import is_valid_number


class MyTestCase(unittest.TestCase):
    def test_valid_whole_positive_number_string(self):
        self.assertTrue(is_valid_number("12345"))

    def test_valid_negative_number_string(self):
        self.assertTrue(is_valid_number("-12345"))

    def test_invalid_negative_number_with_string(self):
        self.assertFalse(is_valid_number("-123-123"))
        self.assertFalse(is_valid_number("-123asd"))
        self.assertFalse(is_valid_number("123asd"))

    def test_alphabetical_string_negative(self):
        self.assertFalse(is_valid_number("asd"))
        self.assertFalse(is_valid_number("-asd"))

    def test_valid_decimal_number(self):
        self.assertTrue(is_valid_number("12.34"))

    def test_invalid_decimal_number(self):
        self.assertFalse(is_valid_number("12..34"))


if __name__ == '__main__':
    unittest.main()
