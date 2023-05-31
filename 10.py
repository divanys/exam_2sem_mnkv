# Сгенерировать матрицу, в которой нечетные элементы заменяются на 0
from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] % 2 == 1:
            matrix[i][j] = 0        

# Вывод результатов
print('Вывод полученной матрицы:')
for i in matrix:
    print(*i, sep='\t')