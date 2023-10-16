# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла, возвращайтесь в его начало.


from task1 import rnd_num
from task2 import rnd_name_in_file


def len_list(list1, list2):
    if len(list2) > len(list1):
        temp = len(list1)
    for i in range(len(list2)):
        if i > len(list1) - 1:
            list1.append(list1[i % temp])
        elif len(list2) < len(list1):
            temp = len(list2)
    for i in range(len(list1)):
        if i > len(list2) - 1:
            list2.append(list2[i % temp])
    return list1, list2


def open_file(file_names, file_num, output):
    with (
        open(file_names, 'r') as a,
        open(file_num, 'r') as b,
        open(output, 'w') as c):
        names = a.read().split('\n')
        num = b.read().split('\n')
        for i, j in zip(*len_list(names, num)):
            if j == '':
                continue
            first, second = map(float, j.split('|'))
            mult = first * second
            if mult < 0:
                c.write(f'{i.lower()} {abs(mult)}\n')
            elif mult > 0:
                c.write(f'{i.upper()} {int(mult)}\n')


if __name__ == '__main__':
    rnd_num(count=10, file_name='num1.txt')
    rnd_name_in_file(count=5, file_name='names1.txt')
    open_file(file_names='names1.txt', file_num='num1.txt', output='output.txt')