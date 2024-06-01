import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.logging_settings import use_logger

new_log = use_logger(__name__)


def convert_json_file(path: str) -> Any:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        new_log.info("Unpacking json...")
        with open(path) as file:
            data = json.load(file)
    except FileNotFoundError:
        new_log.info("FileNotFoundError: return []")
        return []

    else:
        if isinstance(data, list):
            new_log.info("json successfully opened")
            return data
        else:
            new_log.info("json type is not list: return []")
            return []


load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(operations: dict) -> float:
    """которая принимает на вход транзакцию и возвращает сумму транзакции в рублях, возвращает тип float"""
    code = operations["operationAmount"]["currency"]["code"]
    if code == "RUB":
        new_log.info("currency of transaction is RUB")
        return float(operations["operationAmount"]["amount"])
    amount = operations["operationAmount"]["amount"]
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{code}"
    new_log.info("Request to URL")
    respond = requests.get(url)
    new_log.info("Respond has been received")
    json_currency = respond.json()
    new_log.info(f"current course {code}")
    return float(amount) * float(json_currency["conversion_rates"]["RUB"])
