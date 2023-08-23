from datetime import datetime

from utils.func import filter_executed, five_new_operation_sorted_for_date, norm_format_date, convert_from_to, result_data
from setting.path import JSON

def test_filter_executed():
    data = [
        {"state": "EXECUTED"},
        {"state": "PENDING"},
        {"state": "EXECUTED"},
        {"state": "CANCELLED"},
        {"state": "EXECUTED"}
    ]
    expected_result = [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"},
        {"state": "EXECUTED"}
    ]
    assert filter_executed(data) == expected_result


def test_five_new_operation_sorted_for_date():
    executed_operation = [
        {"date": "2021-01-01T10:00:00.000Z"},
        {"date": "2021-01-02T10:00:00.000Z"},
        {"date": "2021-01-03T10:00:00.000Z"},
        {"date": "2021-01-04T10:00:00.000Z"},
        {"date": "2021-01-05T10:00:00.000Z"},
        {"date": "2021-01-06T10:00:00.000Z"}
    ]
    expected_result = [
        {"date": "2021-01-06T10:00:00.000Z"},
        {"date": "2021-01-05T10:00:00.000Z"},
        {"date": "2021-01-04T10:00:00.000Z"},
        {"date": "2021-01-03T10:00:00.000Z"},
        {"date": "2021-01-02T10:00:00.000Z"}
    ]
    assert five_new_operation_sorted_for_date(executed_operation) == expected_result


def test_norm_format_date():
    date = "2021-01-01T10:00:00.000Z"
    expected_result = "01.01.2021"
    assert norm_format_date(date) == expected_result


def test_convert_from_to():
    assert convert_from_to("Счет 35383033474447895560") == "Счет **5560"
    assert convert_from_to("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"


def test_result_data():
    data = {
        "date": "2021-01-01T10:00:00.000Z",
        "description": "Описание операции",
        "from": "Счет 1234567890",
        "to": "Имя Фамилия 1234567890",
        "operationAmount": {
            "amount": "100.50",
            "currency": {
                "name": "USD"
            }
        }
    }
    expected_result = "01.01.2021 Описание операции\n" \
                      "Счет **7890 -> Имя Фамилия 1234 56** **** 7890\n" \
                      "100.50 USD\n"
    assert result_data(data) == expected_result