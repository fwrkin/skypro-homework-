import os.path
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.reading_csv_and_xlsx_files import reading_csv_files, reading_xlsx_files


@patch("pandas.read_csv")
def test_reading_csv_files(mock_read: Mock) -> None:
    """тест для функции reading_csv_files"""
    mock_read.return_value = DataFrame({"test": ["test"]})
    assert reading_csv_files(os.path.join("..", "data", "transactions.csv")) == [{"test": "test"}]


@patch("pandas.read_excel")
def test_reading_xlsx_files(mock_read: Mock) -> None:
    """тест для функции reading_xlsx_files"""
    mock_read.return_value = DataFrame({"test": ["test"]})
    assert reading_xlsx_files(os.path.join("..", "data", "transactions_excel.xlsx")) == [{"test": "test"}]
