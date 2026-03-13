import logging


def log_and_print(message: str, level: int = logging.INFO) -> None:
    """Функция, выводящая сообщение пользователю и записывающая его в лог
    с указанным уровнем
    :param message: сообщение
    :param level: уровень логирования
    :return: ничего не возвращает"""
    print(message)
    logging.log(level, message)
