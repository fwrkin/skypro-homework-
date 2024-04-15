def mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    masked_number = ""
    for num in range(len(card_number)):
        if num < 6 or num >= 12:
            masked_number += card_number[num]
        else:
            masked_number += "*"
        if num == 3 or num == 7 or num == 11:
            masked_number += " "

    return masked_number


def mask_account_number(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    masked_number = account_number[:-4].replace(account_number[:-4], "**") + account_number[-4:]
    return masked_number
