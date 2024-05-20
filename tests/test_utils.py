import json
import os.path
from unittest.mock import Mock, patch

import pytest

from src.utils import convert_json_file, transaction_amount


@pytest.mark.parametrize("value, data", ([[{"key": "value"}], [{"key": "value"}]], [{}, []]))
@patch("builtins.open", create=True)
def test_convert_json_file(mock_open: Mock, value: list | dict, data: list) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps(value)
    assert convert_json_file(os.path.join("..", "data", "operations.json")) == data
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"))


@patch("requests.get")
def test_transaction_amount(mock_get: Mock) -> None:
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 52.99}}
    assert (
        transaction_amount(
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        == 4192300.1407
    )


def test_transaction_amount_rub() -> None:
    assert (
        transaction_amount(
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
            }
        )
        == 79114.93
    )
