import logging
import argparse


logging.basicConfig(filename='logs.log', level=logging.INFO, encoding='utf-8', format='%(asctime)s - %(levelname)s - %(message)s')


class Archive:
    def __init__(self, text, number):
        if not isinstance(text, str) or not text:
            raise TypeError(f"Неверный текст: {text}. Текст должен быть непустой строкой.")

        if not isinstance(number, (int, float)) or not number:
            raise TypeError(f"Неверный номер: {number}. Число должно быть положительным целым числом или числом с плавающей запятой.")

        self.text = text
        self.number = number

    def __str__(self):
        logging.info(f"Текст {self.text} и номер {self.number}")
        return f"Текст {self.text} и номер {self.number}."

def main():
    parser = argparse.ArgumentParser(description="Создать экземпляр архива")
    parser.add_argument("--text", type=str, help="Текст для архива")
    parser.add_argument("--number", type=float, help="Номер для архива")
    args = parser.parse_args()

    if args.text is not None and args.number is not None:
        try:
            archive = Archive(args.text, args.number)
            print(archive)
        except Exception as e:
            logging.error(f"Ввод должен быть текстового формата: {e}")
            print(f"Ввод должен быть текстового формата: {e}")
        except Exception as e:
            logging.error(f"Ввод должен быть числового формата: {e}")
            print(f"Ввод должен быть числового формата: {e}")

if __name__ == "__main__":
    main()