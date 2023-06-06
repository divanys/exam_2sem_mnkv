# Сгенерировать матрицу на произвольное количество элементов, в
# которой задается преобразование от предыдущего элемента к
# следующему на произвольное значение.


from random import randint


rows = randint(3, 9)
columns = randint(3, 9)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] #создание матрицы

transformed_matrix = [[matrix[i][j] + randint(-5, 5) for j in range(columns)] for i in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(*row, sep='\t')

print("\nПреобразованная матрица:")
for row in transformed_matrix:
    print(*row, sep='\t')
