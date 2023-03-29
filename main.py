import sqlalchemy as db
import pandas


class Database:
    def find_least_squares(self, x, y):
        sum = 0
        for i in range(len(x)):
            sum += (x[i] - y[i]) ** 2
        return sum


class Train(Database):
    def load_training_data(self):
        train = pandas.read_csv("dataset/train.csv")
        columns = []
        for train_column in train.columns:
            columns.append(train_column)
        return columns


class Test(Database):
    def load_test_data(self):
        test = pandas.read_csv("dataset/test.csv")
        columns = []
        for test_column in test.columns:
            columns.append(test_column)
        return columns


class Ideal(Database):
    def load_ideal_data(self):
        ideal = pandas.read_csv("dataset/ideal.csv")
        columns = []
        for ideal_column in ideal.columns:
            columns.append(ideal_column)
        return columns


def find_ideal(x, list_of_y):
    least_squares = []
    database = Database()
    for y in list_of_y:
        least_square = database.find_least_squares(x, y)
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
    train = Train()
    test = Test()
    ideal = Ideal()

    train_columns = train.load_training_data()
    test_columns = test.load_test_data()
    ideal_columns = ideal.load_ideal_data()

    least_squares = find_ideal(test_columns, ideal_columns)
    print(train_columns[least_squares])
