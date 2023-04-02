import pandas
import math

"""You need to write a program using Python to choose the best four ideal functions from a set of fifty functions based on how well they fit the training data. 
Then you must use the test data to determine whether each point can be assigned to the four chosen functions, and if so, 
map it to the function with the least deviation. The program must then save the mapping and deviation information and display it visually. 
Finally, you must ensure that any deviations between the mapped data and the ideal functions do not exceed the largest deviation between the training 
set and the ideal function by a factor of sqrt(2)."""


class Database:
    def find_sum_of_least_squares(self, x, y):
        return sum((x - y) ** 2)

    def find_least_squares(self, x, y):
        return (x - y) ** 2

    def find_deviation(self, x, y):
        return x - y


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
        for i in range(len(self.ideal.columns)):
            least_squares.append(database.find_sum_of_least_squares(x, self.ideal.iloc[:, i]))
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
    # Creating instances of train, test and ideal classes
    train = Train()
    test = Test()
    ideal = Ideal()

    # Loading data
    train_data = train.load_training_data()
    test_data = test.load_test_data()
    ideal_data = ideal.load_ideal_data()

    database = Database()

    # Finding ideal functions
    ideal_functions = ideal.find_ideal(train_data.iloc[:, 1])

    # Finding deviation between training and ideal functions
    deviation_between_training_and_ideal = []
    for i in range(len(ideal_functions.columns)):
        deviation_between_training_and_ideal.append(
            database.find_deviation(train_data.iloc[:, 1], ideal_functions.iloc[:, i]))
    deviation_between_training_and_ideal = pandas.DataFrame(deviation_between_training_and_ideal).transpose()

    # Finding maximum deviation
    absolute_deviation = deviation_between_training_and_ideal.abs()
    maximum_deviation = absolute_deviation.max().max()

    # Calculating sqrt(2) * maximum deviation
    sqrt_2 = math.sqrt(2)
    sqrt_2_maximum_deviation = sqrt_2 * maximum_deviation

    # Finding deviation between test and ideal functions
    deviation_between_test_and_ideal = pandas.DataFrame(test_data.iloc[:, 0])
    for i in range(len(ideal_functions.columns)):
        ideal_function = ideal_functions.iloc[:, i]
        print(ideal_function)
        test_data_y = test_data.iloc[:, 1]
        deviation_between_test_and_ideal['Deviation {}'.format(i + 1)] = database.find_deviation(test_data_y,
                                                                                                 ideal_function)

    # Finding absolute deviation between test and ideal functions
    absolute_deviation_between_test_and_ideal = deviation_between_test_and_ideal.abs()
    deviation_greater_than_sqrt_2_maximum_deviation = (
            absolute_deviation_between_test_and_ideal > sqrt_2_maximum_deviation).any()
    print(sqrt_2_maximum_deviation)
    print(deviation_greater_than_sqrt_2_maximum_deviation)
