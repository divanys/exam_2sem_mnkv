# В матрице найти сумму отрицательных элементов в первой трети
# матрицы.

from random import randint, randrange


rows = randrange(3, 9, 3)
columns = randint(3, 9)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] #создание матрицы


third_size = len(matrix) // 3
sum_negative = sum(element for row in matrix[:third_size] for element in row if element < 0)

# Вывод результатов
print("Матрица:")
for row in matrix:
    print(row, sep='\t')

print("Первая треть матрицы:")
for row in matrix[:third_size]:
    print(row)

print("Сумма отрицательных элементов 1/3 матрицы: ", sum_negative)
