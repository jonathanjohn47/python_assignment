import sqlalchemy as db
import pandas

"""You need to write a program using Python to choose the best four ideal functions from a set of fifty functions based on how well they fit the training data. 
Then you must use the test data to determine whether each point can be assigned to the four chosen functions, and if so, 
map it to the function with the least deviation. The program must then save the mapping and deviation information and display it visually. 
Finally, you must ensure that any deviations between the mapped data and the ideal functions do not exceed the largest deviation between the training 
set and the ideal function by a factor of sqrt(2)."""


class Database:
    def find_sum_of_least_squares(self, x, y):
        sum = 0
        for i, j in zip(x, y):
            sum += (i - j) ** 2
        return sum

    def find_least_squares(self, x, y):
        least_squares = []
        for i, j in zip(x, y):
            least_squares.append((i - j) ** 2)
        return least_squares

    def find_deviation(self, x, y):
        deviation = []
        for i, j in zip(x, y):
            deviation.append(i - j)
        return deviation


class Train(Database):
    def load_training_data(self):
        train = pandas.read_csv("dataset/train.csv")
        return train


class Test(Database):
    def load_test_data(self):
        test = pandas.read_csv("dataset/test.csv")
        return test


class Ideal(Database):
    def load_ideal_data(self):
        ideal = pandas.read_csv("dataset/ideal.csv")
        return ideal


def find_ideal(x, y):
    least_squares = []
    database = Database()
    for i in range(len(y.columns)):
        least_squares.append(database.find_sum_of_least_squares(x, y.iloc[:, i]))
    first_four_least_squares = sorted(least_squares)[:4]
    indices = []
    for i in first_four_least_squares:
        indices.append(least_squares.index(i))
    ideal_functions = []
    for i in indices:
        ideal_functions.append(y.iloc[:, i])

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
    ideal_functions = find_ideal(train_data.iloc[:, 1], ideal_data)
    print(ideal_functions)
