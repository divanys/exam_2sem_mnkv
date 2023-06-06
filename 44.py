# Для каждой строки матрицы с нечетным номером найти среднее
# арифметическое ее элементов.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_for_1 = []
for i in range(rows):
    if i % 2 == 0:
        lst_for_1.append(matrix[i])

# Вывод результатов
print('Вывод результата:', *['среднее арифметическое чисел ' + str(lst_for_1[i]) + ' равно ' + str(sum(lst_for_1[i])/len(lst_for_1[i])) for i in range(len(lst_for_1))], sep='\n')
