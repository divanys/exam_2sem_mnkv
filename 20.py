# В матрице найти среднее арифметическое положительных элементов.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_for_positive = []
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] > 0:
            lst_for_positive.append(matrix[i][j])

# Вывод результатов
print(f'Вывод результата: \nсреднее арифметическое чисел {lst_for_positive} равно {sum(lst_for_positive)/len(lst_for_positive)}')
