# В матрице найти минимальный элемент в предпоследнем столбце.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_min_element = []
for i in range(rows):
    lst_min_element.append(matrix[i][-2])
print(f'Минимальный элемент в предпоследнем столбце {lst_min_element}: {min(lst_min_element)}')

