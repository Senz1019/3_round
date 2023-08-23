from setting.path import JSON
from utils.func import five_new_operation_sorted_for_date, filter_executed, open_file, result_data


def main(path):
    for operation in five_new_operation_sorted_for_date(filter_executed(open_file(path))):
        print(result_data(operation))


if __name__ == '__main__':
    main(JSON)