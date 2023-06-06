# В матрице найти среднее арифметическое положительных элементов,
# кратных 3

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

lst_for_sum = []

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] % 3 == 0 and matrix[i][j] > 0 :
            lst_for_sum.append(matrix[i][j])

# Вывод результатов
print(f'Вывод результата:\n среднее арифметическое чисел {lst_for_sum} равно: {sum(lst_for_sum)/len(lst_for_sum)}' if len(lst_for_sum) > 0 else 'В матрице нет положительных элементов, кратных 3')