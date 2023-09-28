# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

fraction_1 = input('Введите первую дробь в формате "a/b": ')
fraction_2 = input('Введите вторую дробь в формате "a/b": ')

a, b = map(int, fraction_1.split("/"))
c, d = map(int, fraction_2.split("/"))

summa_num = a * d + c * b
summa_den = b * d

gcd_summa = gcd(summa_num, summa_den)


multiplay_num = a * c
multiplay_den = b * d

gcd_multiplay = gcd(multiplay_num, multiplay_den)


summa_num_result = summa_num // gcd_summa
summa_den_result = summa_den // gcd_summa

multiplay_num_result = multiplay_num // gcd_multiplay
multiplay_den_result = multiplay_den // gcd_multiplay


if summa_den_result == 1:
    print(f"Сумма дробей: {summa_num_result}")
else:
    print(f"Сумма дробей: {summa_num_result}/{summa_den_result}")

if multiplay_den_result == 1:
    print(f"Произведение дробей: {multiplay_num_result}")
else:
    print(f"Произведение дробей: {multiplay_num_result}/{multiplay_den_result}")



fractions1 = Fraction(a, b)
fractions2 = Fraction(c, d)

summa_fract = fractions1 + fractions2
print(f"Сумма дробей, с использованием собственной функции = {summa_fract}")

multiplay_fract = fractions1 * fractions2
print(f"Произведение дробей, с использованием собственной функции = {multiplay_fract}")