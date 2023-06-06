# В матрице найти суммы элементов каждой строки и поместить их в
# новый массив. Выполнить замену элементов третьего столбца исходной
# матрицы на полученные суммы.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_element, sum_element = [], []
for j in range(rows):
    for i in range(columns):
        lst_element.append(matrix[j][i])
    sum_element.append(sum(lst_element))
    lst_element.clear()
print(f'Сумма элементов: {sum_element} ')


for j in range(len(sum_element)):
    matrix[j][2] = sum_element[j]

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')
