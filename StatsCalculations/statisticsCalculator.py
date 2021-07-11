from Calculator.calculator import Calculator
from StatsCalculations.mean import mean
from StatsCalculations.median import median
from StatsCalculations.mode import mode
from StatsCalculations.variance import variance
from StatsCalculations.standardDeviation import standard_deviation


class StatisticsCalculator(Calculator):

    result = 0

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result


# Source for mean, median, and mode:
#   https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
# Source for variance: https://www.geeksforgeeks.org/python-variance-of-list/
# Source for standard deviation: https://www.geeksforgeeks.org/python-standard-deviation-of-list/
