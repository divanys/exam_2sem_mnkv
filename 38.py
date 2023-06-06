# Перенести в новую матрицу Matr1 элементы, которые не находятся в
# первых и последних сроках и столбцах матрицы Matr2 произвольного
# размера.


from random import randint


rows = randint(3, 6)
colums = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы

Matr1 = [row[1:-1] for row in matrix[1:-1]]

# Вывод результатов
print("matrix:")
for i in matrix:
    print(*i, sep='\t')


print("Matr1:")
for row in Matr1:
    print(*row, sep='\t')


