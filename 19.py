# В матрице элементы третьей строки заменить элементами из
# одномерного массива соответствующей размерности.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')


new_lst = [randint(20, 30) for i in range(columns)]

for i in range(rows):
    for j in range(columns):
        matrix[2][j] = new_lst[j] 


# Вывод результатов
print('Вывод полученной матрицы:')
for i in matrix:
    print(*i, sep='\t')