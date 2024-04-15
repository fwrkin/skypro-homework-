from src.masks import mask_card_number, mask_account_number

def mask_card_or_account_number(data: str) -> str:
    """Принимает на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращает исходную строку с замаскированным номером карты/счета"""
    if "Счет" in data:
        return f"Счет {mask_account_number(data)}"
    else:
        card_data_with_number = data.split(' ')
        card_number = "".join(card_data_with_number[-1])
        if len(card_data_with_number) == 3:
            return f"{' '.join(card_data_with_number[:-1])} {mask_card_number(card_number)}"
        return f"{card_data_with_number[0]} {mask_card_number(card_number)}"

