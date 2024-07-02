import re
from collections import Counter


def change_data(data: list[dict], key_meaning: str = "EXECUTED") -> list[dict]:
    """
    принимает на вход список словарей и значение для ключа state и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение
    """
    updated_list = []
    for item in data:
        if item.get("state", "") == key_meaning:
            updated_list.append(item)
    return updated_list


def sorted_by_data(data: list[dict], reversed: bool = True) -> list[dict]:
    """
    принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты
    """
    new_data = sorted(data, key=lambda x: x.get("date", ""), reverse=reversed)
    return new_data


def find_description(bank_list: list, found_line: str) -> list:
    """
    принимает список словарей с данными о банковских операциях и строку поиска и
    возвращает список словарей, у которых в описании есть данная строка
    """
    new_list = []
    for elem in bank_list:
        if re.search(found_line.lower(), elem["description"].lower()):
            new_list.append(elem)
    return new_list


def counter_of_operations(data_list: list, category_list: list) -> dict:
    """
    принимает список словарей с данными о банковских операциях и список категорий операций и возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    list_ = []
    for element in data_list:
        if element["description"] in category_list:
            list_.append(element["description"])
    return Counter(list_)
