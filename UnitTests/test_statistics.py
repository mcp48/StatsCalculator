import unittest
from StatsCalculations.statisticsCalculator import StatisticsCalculator
from CSVReader.csv_reader import CSVReader
from RandomGenerator.randomIntegerList import random_integer_list
from numpy import var, std


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statsCalc = StatisticsCalculator()
        self.allData = CSVReader('./UnitTests/TestData/Stats_Test_Data.csv').data
        self.testData = [int(row['Value']) for row in self.allData]
        self.testAnswers = CSVReader('./UnitTests/TestData/Stats_Answers.csv').data
        self.list = random_integer_list(1, 100, 20, 10)
        self.num_val = 4

    def test_instantiate_stats_calculator(self):
        self.assertIsInstance(self.statsCalc, StatisticsCalculator)

    def test_mean(self):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.mean(self.testData), float(row['Mean']))
            self.assertEqual(self.statsCalc.result, float(row['Mean']))

    def test_median(self):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.median(self.testData), float(row['Median']))
            self.assertEqual(self.statsCalc.result, float(row['Median']))

    def test_mode(self):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.mode(self.testData), float(row['Mode']))
            self.assertEqual(self.statsCalc.result, float(row['Mode']))

    def test_variance_method(self):
        var_test_val = (var(self.testData))
        self.assertEqual(self.statsCalc.variance(self.testData), var_test_val)
        self.assertEqual(self.statsCalc.result, var_test_val)


if __name__ == '__main__':
    unittest.main()
