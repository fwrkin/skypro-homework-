from src.decorators import log


@log(filename="test_decorators.txt")
def sum_(ex: str) -> str:
    return "artem" + ex


def test_log_artem() -> None:
    sum_("mama")
    with open("test_decorators.txt", "r", encoding="UTF-8") as file:
        line = file.readlines()[-1].strip()
    assert line == "sum_ ok"


def test_log_artem_second_attempt() -> None:
    sum_(4)
    with open("test_decorators.txt", "r", encoding="UTF-8") as file:
        line = file.readlines()[-1].strip()
    assert line == 'sum_ error: can only concatenate str (not "int") to str. Inputs: ((4,), {})'
