# В матрице отрицательные элементы возвести в квадрат.


from random import randint


rows = randint(3, 6)
colums = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы

result = []

for i in range(rows):
    for j in range(colums):
        if matrix[i][j] < 0:
            result.append(matrix[i][j]**2)


# Вывод результатов
print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

print('Вывод результата: \n', result)