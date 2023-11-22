import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, encoding='utf-8',format='%(asctime)s - %(levelname)s - %(message)s')

def my_func(storage, key, value=None):
    try:
        return storage[key]
    except KeyError:
        logging.error(f"Отсутствует ключ {key} в словаре {storage}")
        return value

f={'f':'1', 'd':'3', 's':'5'}
print (my_func (f, key='a', value=2))

# 2023-11-22 11:38:17,261 - ERROR - Отсутствует ключ a в словаре {'f': '1', 'd': '3', 's': '5'}