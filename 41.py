# В матрице найти минимальный элемент в предпоследней строке

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_min_element = []
for i in range(columns):
    lst_min_element.append(matrix[-2][i])
print(f'Минимальный элемент в предпоследней строке {lst_min_element}: {min(lst_min_element)}')

