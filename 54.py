# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.



from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

n = int(input('Введите число N: '))
print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')

for i in range(rows):
    for j in range(columns):
            if i == (n - 1): 
                matrix[i][j] += 3

# Вывод результатов
print('Вывод полученной матрицы:')
for i in matrix:
    print(*i, sep='\t')