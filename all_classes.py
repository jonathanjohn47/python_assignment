import pandas
import numpy as np


class Database:
    def find_sum_of_least_squares(self, x, y):
        x = np.array(x)
        y = np.array(y)
        difference = np.subtract(x, y)
        square = np.square(difference)
        sumOfSquares = np.sum(square)

        return sumOfSquares

    def find_least_squares(self, x, y):
        x = np.array(x)
        y = np.array(y)
        difference = np.subtract(x, y)
        square = np.square(difference)
        return pandas.DataFrame(square)

    def find_deviation(self, x, y):
        x = np.array(x)
        y = np.array(y)
        difference = np.subtract(x, y)
        return pandas.DataFrame(difference)

    def any_deviation_greater_than_threshold(self, x, y, threshold):
        x = np.array(x)
        y = np.array(y)
        difference = pandas.DataFrame(np.subtract(x, y))

        return (difference > threshold).any().any()


class Train(Database):
    def load_training_data(self):
        self.train = pandas.read_csv("dataset/train.csv")
        return self.train

    def get_deviation(self, x):
        self.deviation = self.find_deviation(x, self.train.iloc[:, 1])
        return self.deviation


class Test(Database):
    def load_test_data(self):
        self.test = pandas.read_csv("dataset/test.csv")
        return self.test


class Ideal(Database):
    def load_ideal_data(self):
        self.ideal = pandas.read_csv("dataset/ideal.csv")
        return self.ideal

    def find_ideal(self, x):
        database = Database()
        least_squares = [database.find_sum_of_least_squares(x, self.ideal.iloc[:, i]) for i in
                         range(len(self.ideal.columns))]

        first_four_least_squares = sorted(least_squares)[:4]
        indices = [least_squares.index(i) for i in first_four_least_squares]
        ideal_functions = [self.ideal.iloc[:, i] for i in indices]

        ideal_functions = pandas.DataFrame(ideal_functions).transpose()
        ideal_functions.columns = ['y1', 'y2', 'y3', 'y4']
        return ideal_functions
