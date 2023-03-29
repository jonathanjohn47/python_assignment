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
        self.train = pandas.read_csv("dataset/train.csv")


class Test(Database):
    def load_test_data(self):
        self.test = pandas.read_csv("dataset/test.csv")


class Ideal(Database):
    def load_ideal_data(self):
        self.ideal = pandas.read_csv("dataset/ideal.csv")


if __name__ == "__main__":
