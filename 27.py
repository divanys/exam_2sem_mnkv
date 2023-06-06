# Для каждого столбца матрицы с четным номером найти сумму ее
# элементов.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')
column_sums = [0] * columns

for j in range(columns):
    if j % 2 == 1:  # проверяем, является ли номер столбца четным
        column_sum = 0
        for i in range(rows):
            column_sum += matrix[i][j]
        column_sums[j] = column_sum

print("Суммы элементов столбцов с четным номером:")
for j in range(columns):
    if j % 2 == 0:
        print(f"Столбец {j + 1}: {column_sums[j]}")