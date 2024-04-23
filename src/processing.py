def change_data(data: list[dict], key_meaning: str = "EXECUTED") -> list[dict]:
    """
    принимает на вход список словарей и значение для ключа state и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение
    """
    updated_list = []
    for item in data:
        if item["state"] == key_meaning:
            updated_list.append(item)
    return updated_list


def sorted_by_data(data: list[dict], reversed: bool = True) -> list[dict]:
    """
    принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты
    """
    new_data = sorted(data, key=lambda x: x["date"], reverse=reversed)
    return new_data
