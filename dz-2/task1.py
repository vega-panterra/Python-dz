# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input("Введите целое число в десятичной системе: "))
print(f'Встроенная функция hex = {hex(number)}')

def to_hex(number):
    hex_dec_rule = "0123456789ABCDEF"
    hex_str = " "

    while number > 0:
        hex_str = hex_dec_rule[number % 16] + hex_str
        number = number // 16
    return '0x'+ hex_str

print(f'Собственная функция = {to_hex(number)}')