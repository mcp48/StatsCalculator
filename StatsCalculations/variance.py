from Calculator.square import square
from Calculator.division import division
from StatsCalculations.mean import mean


def variance(data):
    try:
        mean_of_data = mean(data)
        total_values = len(data)
        v = 0
        for a in data:
            v = v + square(a - mean_of_data)
        result = division(v, total_values)

        return result

    except ValueError:
        print("ERROR: That is an emtpy array! Try again.")
