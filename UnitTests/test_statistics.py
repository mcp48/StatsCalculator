import unittest
from StatsCalculations.statisticsCalculator import StatisticsCalculator
from CSVReader.csv_reader import CSVReader
from RandomGenerator.randomIntegerList import random_integer_list
from numpy import var, std, mean
from pprint import pprint


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


if __name__ == '__main__':
    unittest.main()
