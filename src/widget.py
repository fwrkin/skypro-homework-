from src.masks import mask_account_number, mask_card_number


def mask_card_or_account_number(data: str) -> str:
    """Принимает на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета"""
    if "Счет" in data:
        return f"Счет {mask_account_number(data)}"
    else:
        card_data_with_number = data.split(" ")
        card_number = "".join(card_data_with_number[-1])
        if len(card_data_with_number) == 3:
            return f"{' '.join(card_data_with_number[:-1])} {mask_card_number(card_number)}"
        return f"{card_data_with_number[0]} {mask_card_number(card_number)}"


def get_new_type_of_date(date: str) -> str:
    """возвращает строку с датой в нужном нам виде"""
    type_of_date = date.split("T")
    date_ = type_of_date[0].split("-")
    return f"{date_[2]}.{date_[1]}.{date_[0]}"
