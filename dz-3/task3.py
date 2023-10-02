# 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.

def backpack():
    things = {
        'теплая одежда': 2,
        'нож': 1,
        'фонарик': 1,
        'спальник': 3,
        'палатка': 4,
        'еда': 3,
        'фляга': 1,
        'посуда': 2,
        'коврик': 2,
        'аптечка': 1
    }

    backpack = int(input('Введите максимальную грузоподъемность рюкзака: '))
    list_things = list(things.keys())
    result, temp, weight = set(), [], 0

    for i in range((2 ** len(things))):
        sample = (list(bin(i)[2:].zfill(len(things))))
        for n in range(len(sample)):
            if sample[n] == '1':
                temp.append(list_things[n])
                weight += things[list_things[n]]
                if weight > backpack:
                    temp.pop()
                    break
        result.add(', '.join(temp))
        temp, weight = [], 0

    print('Все возможные варианты комплектации рюкзака:')
    for i in result:
        yield i if len(i) > 0 else 'пустой рюкзак'

if __name__ == '__main__':
    print(*backpack(), sep=';\n', end='.')