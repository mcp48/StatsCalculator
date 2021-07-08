import unittest
from Calculator.calculator import calculator
from CSVReader.csv_reader import CSVReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_add_method_calculator(self):
        test_data = CSVReader('./UnitTests/TestData/Unit_Tests_Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))
