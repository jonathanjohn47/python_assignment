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
        for i in range(len(x)):
            sum += (x[i] - y[i]) ** 2
        return sum

    def find_least_squares(self, x, y):
        least_squares = []
        for i in range(len(x)):
            least_squares.append((x[i] - y[i]) ** 2)
        return least_squares

    def find_deviation(self, x, y):
        deviation = []
        for i in range(len(x)):
            deviation.append(x[i] - y[i])
        return deviation


class Train(Database):
    def load_training_data(self):
        train = pandas.read_csv("dataset/train.csv")
        columns = []
        for i in range(train.shape[1]):
            this_column = []
            for j in range(train.shape[0]):
                this_column.append(train.iloc[j, i])
            columns.append(this_column)
        return columns


class Test(Database):
    def load_test_data(self):
        test = pandas.read_csv("dataset/test.csv")
        columns = []
        for i in range(test.shape[1]):
            this_column = []
            for j in range(test.shape[0]):
                this_column.append(test.iloc[j, i])
            columns.append(this_column)
        return columns


class Ideal(Database):
    def load_ideal_data(self):
        ideal = pandas.read_csv("dataset/ideal.csv")
        columns = []
        for i in range(ideal.shape[1]):
            this_column = []
            for j in range(ideal.shape[0]):
                this_column.append(ideal.iloc[j, i])
            columns.append(this_column)
        return columns


def find_ideal(x, list_of_y):
    least_squares = []
    database = Database()
    for y in list_of_y:
        least_square = database.find_sum_of_least_squares(x, y)
        least_squares.append(least_square)
    least_four_squares = sorted(least_squares)[:4]
    indices = []
    for least_four_square in least_four_squares:
        indices.append(least_squares.index(least_four_square))
    sorted_y = []
    for index in indices:
        sorted_y.append(list_of_y[index])
    return sorted_y


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

    ideal_functions = find_ideal(train_data[1], ideal_data)

