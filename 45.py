# В матрице найти максимальный положительный элемент, кратный 4.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 20) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

try:
    lst_max_element = []
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] % 4 == 0 and matrix[i][j] > 0:
                lst_max_element.append(matrix[i][j])
    print(f'Максимальный положительный элемент, кратный 4: {max(lst_max_element)}')

except:
    max_element = 'В матрице отсутствуют положительные элементы, кратные 4'
    print(max_element)

    