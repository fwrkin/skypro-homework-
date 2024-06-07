import pandas as pd


def reading_csv_files(filename: str) -> list:
    """считывание финансовых операций с CSV файла"""
    data = pd.read_csv(filename, sep=";")
    return data.to_dict("records")


def reading_xlsx_files(filename: str) -> list:
    """считывание финансовых операций с XLSX файла"""
    data = pd.read_excel(filename)
    return data.to_dict("records")
