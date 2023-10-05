# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transposition(matrix):
    result = [list(row) for row in zip(*matrix)]
    return result

matrix = [[1, 2, 3], [4, 5, 6]]
trans_matrix = transposition(matrix)

print(trans_matrix)