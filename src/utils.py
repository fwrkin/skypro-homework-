import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_json_file(path: str) -> Any:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path) as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    else:
        if isinstance(data, list):
            return data
        else:
            return []


load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(operations: dict) -> float:
    """которая принимает на вход транзакцию и возвращает сумму транзакции в рублях, возвращает тип float"""
    code = operations["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return float(operations["operationAmount"]["amount"])
    amount = operations["operationAmount"]["amount"]
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{code}"
    respond = requests.get(url)
    json_currency = respond.json()
    return float(amount) * float(json_currency["conversion_rates"]["RUB"])
