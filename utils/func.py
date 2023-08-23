import datetime
import json
import re

def open_file(path):
    """
    Открыть json файл

    """
    with open(path, encoding="UTF-8") as load_file:
        return json.loads(load_file.read())


def filter_executed(data):
    """
    фильтруем операции по статусу "Выполнено"

    """
    executed_operation = []
    for operation in data:
        if operation.get("state") == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation


def five_new_operation_sorted_for_date(executed_operation):
    """
    Находит 5 новых операций и фильтрует их по дате

    """
    sorted_date = list(sorted(executed_operation,
                              key=lambda operation: operation['date'],
                              reverse=True))[:5]
    return sorted_date


def norm_format_date(date):
    """
    Преобразует дату в обычный формат

    """
    date = date.replace("Z", "")
    date_ = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_.strftime("%d.%m.%Y")


def convert_from_to(data):
    """
    Показывает путь транзакции "Откуда" -> "Куда"

    """
    if data.startswith('Счет'):
        return data[0:5] + "**" + data[-4:]
    else:
        name = ""
        numer = ""
        for i in data:
            if '0' <= i <= '9':
                numer += i
            else:
                name += i
        return f'{name}{numer[0:4]} {numer[4:6]}** **** {numer[-4:]}'

def result_data(data):
    """
    Отображает готовый результат

    """
    date_ = norm_format_date(data["date"])
    description_ = data["description"]
    from_ = convert_from_to(data["from"]) if data.get("from") else ""
    to_ = convert_from_to(data["to"])
    amount_ = data["operationAmount"]["amount"]
    name_ = data["operationAmount"]["currency"]["name"]
    return f'{date_} {description_}\n' \
           f'{from_} -> {to_}\n' \
           f'{amount_} {name_}\n'