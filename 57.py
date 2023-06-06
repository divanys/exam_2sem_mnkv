# В матрице элементы последнего столбца заменить на -1.


from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

for i in range(rows):
    for j in range(columns):
            matrix[i][-1] = -1 

# Вывод результатов
print('Вывод полученной матрицы:')
for i in matrix:
    print(*i, sep='\t')