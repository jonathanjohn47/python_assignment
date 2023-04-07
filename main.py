import pandas
import numpy as np
import math

"""You need to write a program using Python to choose the best four ideal functions from a set of fifty functions based on how well they fit the training data. 
Then you must use the test data to determine whether each point can be assigned to the four chosen functions, and if so, 
map it to the function with the least deviation. The program must then save the mapping and deviation information and display it visually. 
Finally, you must ensure that any deviations between the mapped data and the ideal functions do not exceed the largest deviation between the training 
set and the ideal function by a factor of sqrt(2)."""


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
        least_squares = []
        database = Database()
        least_squares = [database.find_sum_of_least_squares(x, self.ideal.iloc[:, i]) for i in
                         range(len(self.ideal.columns))]

        first_four_least_squares = sorted(least_squares)[:4]
        indices = []
        for i in first_four_least_squares:
            indices.append(least_squares.index(i))
        ideal_functions = []
        for i in indices:
            ideal_functions.append(self.ideal.iloc[:, i])

        ideal_functions = pandas.DataFrame(ideal_functions).transpose()
        ideal_functions.columns = ['y1', 'y2', 'y3', 'y4']
        return ideal_functions


if __name__ == "__main__":

    """Creating instances of train, test and ideal classes"""
    train = Train()
    test = Test()
    ideal = Ideal()

    """Loading data"""
    train_data = train.load_training_data()
    test_data = test.load_test_data()
    ideal_data = ideal.load_ideal_data()

    database = Database()

    """Finding ideal functions"""

    ideal_functions = ideal.find_ideal(train_data.iloc[:, 1])
    ideal_functions.insert(0, 'x', train_data.iloc[:, 0])

    """Finding deviation between training and ideal functions"""
    deviation_between_training_and_ideal = pandas.DataFrame([])
    for column in ideal_functions.columns:
        deviation_between_training_and_ideal[column] = database.find_deviation(train_data.iloc[:, 1],
                                                                               ideal_functions[column])
    deviation_between_training_and_ideal = pandas.DataFrame(deviation_between_training_and_ideal)

    """Finding maximum deviation"""
    absolute_deviation = deviation_between_training_and_ideal.abs()
    maximum_deviation = absolute_deviation.max().max()

    """Calculating sqrt(2) * maximum deviation"""
    sqrt_2 = math.sqrt(2)
    sqrt_2_maximum_deviation = sqrt_2 * maximum_deviation

    """Finding best fit values for test data in ideal functions"""
    x_values = np.array([])
    y1_values = np.array([])
    y2_values = np.array([])
    y3_values = np.array([])
    y4_values = np.array([])

    for t in test_data.iloc[:, 0]:
        least_squares = np.array([])
        for x in ideal_functions.iloc[:, 0]:
            least_squares = np.append(least_squares, (x - t) ** 2)
        index = np.argmin(least_squares)
        x_values = np.append(x_values, ideal_functions.iloc[index, 0])
        y1_values = np.append(y1_values, ideal_functions.iloc[index, 1])
        y2_values = np.append(y2_values, ideal_functions.iloc[index, 2])
        y3_values = np.append(y3_values, ideal_functions.iloc[index, 3])
        y4_values = np.append(y4_values, ideal_functions.iloc[index, 4])

    best_fit_values = pandas.DataFrame([x_values, y1_values, y2_values, y3_values, y4_values]).transpose()
    best_fit_values.columns = ['x', 'y1', 'y2', 'y3', 'y4']
    print(best_fit_values)

    """Finding corresponding y values for x values in ideal functions"""
