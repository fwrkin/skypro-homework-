import os.path

from src.processing import change_data, find_description, sorted_by_data
from src.reading_csv_and_xlsx_files import reading_csv_files, reading_xlsx_files
from src.utils import convert_json_file
from src.widget import get_new_type_of_date, mask_card_or_account_number


def hello() -> list:
    """
    приветствие пользователя
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из json файла")
    print("2. Получить информацию о транзакциях из csv файла")
    print("3. Получить информацию о транзакциях из xlsx файла")
    data_ = []
    user_input = int(input())
    if user_input == 1:
        print("Для обработки выбран json файл.")
        data_ = convert_json_file(os.path.join("data", "operations.json"))
    elif user_input == 2:
        print("Для обработки выбран csv файл.")
        data_ = reading_csv_files(os.path.join("data", "transactions.csv"))
    else:
        print("Для обработки выбран xlsx файл.")
        data_ = reading_xlsx_files(os.path.join("data", "transactions_excel.xlsx"))
    return data_


def filter_status(data: list) -> list:
    """
    запрашивает статус и фильтрует по статусу
    """
    while True:
        print("Введите статус по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_input = input().upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {user_input}")
            data = change_data(data, user_input)
            return data
        else:
            print(f"Статус операции {user_input} недоступен.")


def issue(data: list) -> list:
    """
    спрашивает, нужна ли сортировка по датам, сортирует, если да, оставляет список таким же, если нет
    """
    print("Отсортировать операции по дате? Да/Нет")
    user_input = input().lower()
    if user_input == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input().lower()
        if "возр" in user_input:
            data = sorted_by_data(data, False)
        else:
            data = sorted_by_data(data)
    return data


def filter_rub(data: list) -> list:
    """
    фильтрует по рублю
    """
    print("Выводить только рублевые тразакции? Да/Нет")
    user_input = input().lower()
    if user_input == "да":
        new_data = []
        for item in data:
            for k, v in item.items():
                if k == "operationAmount":
                    if item[k]["currency"]["code"] == "RUB":
                        new_data.append(item)
                elif k == "currency_code":
                    if item[k] == "RUB":
                        new_data.append(item)
        return new_data
    return data


def filter_by_word(data: list) -> list:
    """
    фильтрует по введенному пользователем слову
    """
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input = input().lower()
    if user_input == "да":
        print("По какому слову фильтровать?")
        user_input = input().lower()
        data = find_description(data, user_input)
    return data


def output(data: list) -> None:
    """
    выводит результат
    """
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(data)}")
    amount = ""
    currency = ""
    for elem in data:
        date = get_new_type_of_date(elem.get("date", "9999-77-33T88:55:99.512345"))
        to = mask_card_or_account_number(elem.get("to", ""))
        description = elem.get("description", "")
        if "operationAmount" in elem.keys():
            amount = elem["operationAmount"]["amount"]
            currency = elem["operationAmount"]["currency"]["name"]
        elif "amount" in elem.keys():
            amount = elem["amount"]
            currency = elem["currency_name"]
        if "перевод" in elem["description"].lower():
            from_ = mask_card_or_account_number(elem["from"])
            print(f"{date} {description}")
            print(f"{from_} -> {to}")
            print(f"Сумма: {amount} {currency}")
            print()
        else:
            print(f"{date} {description}")
            print(f"{to}")
            print(f"Сумма: {amount} {currency}")
            print()


if __name__ == "__main__":
    data_ = hello()
    data_ = filter_status(data_)
    data_ = issue(data_)
    data_ = filter_rub(data_)
    data_ = filter_by_word(data_)
    output(data_)
