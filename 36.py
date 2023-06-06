# В матрице найти среднее арифметическое элементов последних двух
# столбцов.

from random import randint


rows = randint(2, 6)
columns = randint(2, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] #создание матрицы

sum_last_columns = 0
for row in matrix:
    sum_last_columns += row[-1] + row[-2]

average = sum_last_columns / (rows * 2)

print("Матрица:")
for row in matrix:
    print(*row, sep='\t')
    
print("\nСреднее арифметическое элементов последних двух столбцов:", average)
