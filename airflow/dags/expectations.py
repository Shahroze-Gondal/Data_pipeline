import os

import great_expectations as ge
# from great_expectations_provider.example_dags.example_great_expectations_dag import base_path

data_file = os.path.join("include", "/home/shahroze/yellow_tripdata_sample_2019-01.csv")
df = ge.read_csv(data_file)


def check_file():
    if df.empty:
        raise ValueError('File not parsed completely/correctly')
    return True


def expectation1():
    check_success = df.expect_column_values_to_be_in_set('passenger_count', [1, 2, 3, 4, 5])
    if check_success['success']:
        return True
    raise ValueError('Values are not in given set')


def expectation2():
    check_success = df.expect_column_mean_to_be_between('trip_distance', 0, 1)
    if check_success['success']:
        return True
    raise ValueError('Mean is not in given values')


def expectation3():
    check_success = df.expect_column_min_to_be_between('trip_distance', 0, 3)
    if check_success['success']:
        return True
    raise ValueError('Min is not in given values')


def expectation4():
    check_success = df.expect_column_to_exist('trip_distance')
    if check_success['success']:
        return True
    raise ValueError('Given Column does not exist')


def expectation5():
    check_success = df.expect_column_unique_value_count_to_be_between('trip_distance', 1000, 6000)
    if check_success['success']:
        return True
    raise ValueError('Given Column does not exist')

