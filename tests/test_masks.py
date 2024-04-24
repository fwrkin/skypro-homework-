import pytest

from src.masks import mask_account_number, mask_card_number


@pytest.fixture
def data() -> str:
    return "7000792289606361"


def test_mask_card_number(data: str) -> None:
    assert mask_card_number(data) == "7000 79** **** 6361"


@pytest.fixture
def data_account() -> str:
    return "73654108430135874305"


def test_mask_account_number(data_account: str) -> None:
    assert mask_account_number(data_account) == "**4305"
