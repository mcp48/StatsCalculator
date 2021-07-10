from Calculator.square_root import square_root
from StatsCalculations.variance import variance


def standard_deviation(data):
    try:
        variance_of_data = variance(data)
        return square_root(variance_of_data)

    except ValueError:
        print("ERROR!  That is an empty array.  Try again.")
