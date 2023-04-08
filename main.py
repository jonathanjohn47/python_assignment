import pandas
import numpy as np
import math
import all_classes as cl
import sql_classes as sql

if __name__ == "__main__":

    """Creating instances of train, test and ideal classes"""
    train = cl.Train()
    test = cl.Test()
    ideal = cl.Ideal()

    """Loading data"""
    train_data = train.load_training_data()
    test_data = test.load_test_data()
    ideal_data = ideal.load_ideal_data()

    database = cl.Database()

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
        least_squares = np.array([(x - t) ** 2 for x in ideal_functions.iloc[:, 0]])

        index = np.argmin(least_squares)
        x_values = np.append(x_values, ideal_functions.iloc[index, 0])
        y1_values = np.append(y1_values, ideal_functions.iloc[index, 1])
        y2_values = np.append(y2_values, ideal_functions.iloc[index, 2])
        y3_values = np.append(y3_values, ideal_functions.iloc[index, 3])
        y4_values = np.append(y4_values, ideal_functions.iloc[index, 4])

    best_fit_values = pandas.DataFrame([x_values, y1_values, y2_values, y3_values, y4_values]).transpose()
    best_fit_values.columns = ['x', 'y1', 'y2', 'y3', 'y4']

    """Creating tables"""
    y1 = pandas.DataFrame([])
    y2 = pandas.DataFrame([])
    y3 = pandas.DataFrame([])
    y4 = pandas.DataFrame([])

    table_list = [y1, y2, y3, y4]

    """Filling tables"""
    for i in range(1, 5):
        if database.any_deviation_greater_than_threshold(best_fit_values.iloc[:, i], test_data.iloc[:, 1],
                                                         sqrt_2_maximum_deviation):
            print('y' + str(i) + ' is not in range')
        else:
            table_list[i - 1]['x'] = test_data.iloc[:, 0]
            table_list[i - 1]['y'] = test_data.iloc[:, 1]
            table_list[i - 1]['delta'] = database.find_deviation(test_data.iloc[:, 1], best_fit_values.iloc[:, i])
            table_list[i - 1]['ideal function'] = best_fit_values.iloc[:, i]

            """Saving tables to database"""
            test = sql.DataSet('test_' + 'y' + str(i + 1), table_list[i - 1])
            test.execute_sql()

    """Creating Database in SQLite"""
    training = sql.DataSet(best_fit_values, 'training_data')
    training.execute_sql()

    ideal = sql.DataSet(ideal_data, 'ideal_functions')
    ideal.execute_sql()
