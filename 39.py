# В матрице найти сумму элементов первых двух строк

from random import randint


rows = randint(3, 9)
columns = randint(3, 9)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] #создание матрицы


lst_sum = []
for i in range(2):
    for j in range(columns):
        lst_sum.append(matrix[i][j])

print("Исходная матрица:")
for row in matrix:
    print(*row, sep='\t')

print('Сумма равна', sum(lst_sum))