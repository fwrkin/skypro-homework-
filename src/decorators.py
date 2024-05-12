from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """логирует вызов функции и ее результат в файл или в консоль"""

    def my_decorator(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                res = func(*args, **kwargs)
            except Exception as type_of_error:
                if filename is None:
                    print(f"{func.__name__} error: {type_of_error}. Inputs: {args, kwargs}")
                else:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {type_of_error}. Inputs: {args, kwargs}\n")
            else:
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
                return res

        return inner

    return my_decorator
