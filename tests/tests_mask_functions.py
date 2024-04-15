from src.masks import mask_account_number, mask_card_number
from src.widget import get_new_type_of_date, mask_card_or_account_number

print(mask_card_number("8976543624357896"))
print(mask_account_number("89765436243555557896"))
print(mask_card_or_account_number("Visa Platinum 8990922113665229"))
print(mask_card_or_account_number("Счет 35383033474447895560"))
print(mask_card_or_account_number("MasterCard 7158300734726758"))
print(get_new_type_of_date("2018-07-11T02:26:18.671407"))
