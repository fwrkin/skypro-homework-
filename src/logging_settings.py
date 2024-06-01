import logging


def use_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(f"{name}.log", "w", encoding="UTF8")
    file_formatter = logging.Formatter("%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger
