import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, encoding='utf-8',format='%(asctime)s - %(levelname)s - %(message)s')

class InvalidTextError(Exception):
    pass

class InvalidNumberError(Exception):
    pass

class Archive:
    def __init__(self, text, number):
        if not isinstance(text, str) or not text:
            raise InvalidTextError(f"Неверный текст: {text} или пустая строка.")

        if not (isinstance(number, int) and number > 0) and not (isinstance(number, float) and number > 0):
            logging.error(f"Ввод должен быть числового формата: {number}")
            raise InvalidNumberError(f"Неверный номер: {number} или число должно быть положительным целым / число с плавающей запятой.")

        self.text = text
        self.number = number

    def __str__(self):
        logging.info(f"Текст {self.text} и номер {self.number}")
        return f"Текст {self.text} и номер {self.number}."

try:
    archive1 = Archive(42, 42)
    print(archive1)

except InvalidTextError as e:
    logging.error(f"Ввод текстового формата: {e}")
    print(f"Ввод текстового формата: {e}")
except TypeError as e:
    logging.error(f"Ввод числового формата: {e}")
    print(f"Ввод числового формата: {e}")

    # 2023-11-22 11:39:18,702 - ERROR - Ввод текстового формата: Неверный текст: 42 или пустая строка.