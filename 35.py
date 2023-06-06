# В матрице элементы кратные 3 увеличить в 3 раза


from random import randint


rows = randint(2, 6)
columns = randint(2, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] #создание матрицы

print("Исходная матрица:")
for row in matrix:
    print(*row, sep='\t')

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] *= 3

print("Получившаяся матрица:")
for row in matrix:
    print(*row, sep='\t')
