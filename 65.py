# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое.

from random import randint


rows = randint(3, 6)
colums = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] # создание матрицы

result = 0
len_res = 0

for i in range(rows):
    for j in range(colums):
        if matrix[i][j] > 0 and matrix[i][j] % 2 == 0:
            result += matrix[i][j]
            len_res += 1

# Вывод результатов
print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

print(f'Вывод суммы: {result}')
print(f'Вывод среднего арифметического: {result / len_res}')
