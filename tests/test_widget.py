import pytest

from src.widget import get_new_type_of_date, mask_card_or_account_number


@pytest.mark.parametrize(
    "input, output",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_card_or_account_number(input: str, output: str) -> None:
    assert mask_card_or_account_number(input) == output


@pytest.fixture
def date() -> str:
    return "2018-07-11T02:26:18.671407"


def test_get_new_type_of_date(date: str) -> None:
    assert get_new_type_of_date(date) == "11.07.2018"
