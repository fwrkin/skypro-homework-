from typing import Iterator


def filter_by_currency(transactions: list, code: str) -> Iterator:
    """принимает список словарей и возвращает итератор,
    который выдает по очереди операции с заданной валюта.
    """
    for trans in transactions:
        if trans["operationAmount"]["currency"]["code"] == code:
            yield trans


def transaction_descriptions(transactions: list) -> Iterator:
    """принимает список словарей и возвращает
    описание каждой операции по очереди."""
    for trans_ in transactions:
        yield trans_["description"]


def card_number_generator(first: int, last: int) -> Iterator:
    """генерирует номера карт"""
    for num in range(first, last + 1):
        yield f"{num:016d}"
