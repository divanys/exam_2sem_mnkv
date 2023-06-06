# В матрице найти суммы элементов каждого столбца и поместить их в
# новый массив. Выполнить замену элементов второй строки исходной
# матрицы на полученные сумм.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_element, sum_element = [], []
for i in range(columns):
    for j in range(rows):
        lst_element.append(matrix[j][i])
    sum_element.append(sum(lst_element))
    lst_element.clear()
print(f'Сумма элементов: {sum_element} ')


for j in range(len(sum_element)):
    matrix[1][j] = sum_element[j]

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

