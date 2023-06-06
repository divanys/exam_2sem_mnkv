# В матрице найти сумму элементов второй половины матрицы.


from random import randrange, randint


rows = randrange(2, 10, 2)
columns = randint(3, 9)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] #создание матрицы


second_size = len(matrix) // 2
sum_2 = sum(element for row in matrix[second_size:] for element in row)

# Вывод результатов
print("Матрица:")
for row in matrix:
    print(row, sep='\t')

print("Вторая половины матрицы:")
for row in matrix[second_size:]:
    print(row)

print("Сумма второй половины матрицы: ", sum_2)
