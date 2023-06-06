# В квадратной матрице элементы на главной диагонали увеличить в 2
# раза

from random import randint


rows = randint(3, 6)
columns = rows  # Для квадратной матрицы количество столбцов равно количеству строк
matrix = [[randint(-10, 10) for _ in range(columns)] for _ in range(rows)]  # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

for i in range(rows):
    matrix[i][i] *= 2

# Вывод результатов
print('Вывод обновлённой матрицы:')
for i in matrix:
    print(*i, sep='\t')