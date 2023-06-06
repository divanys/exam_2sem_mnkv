# В квадратной матрице все элементы, не лежащие на главной диагонали
# увеличить в 2 раза
from random import randint


rows = randint(2, 6)
columns = rows  # Для квадратной матрицы количество столбцов равно количеству строк
matrix = [[randint(-10, 10) for _ in range(columns)] for _ in range(rows)]  # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

# Увеличение элементов не на главной диагонали в 2 раза
for i in range(rows):
    for j in range(columns):
        if i != j:
            matrix[i][j] *= 2

# Вывод результатов
print('Вывод обновлённой матрицы:')
for i in matrix:
    print(*i, sep='\t')