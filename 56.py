# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')
    
n = int(input('Введите число N: '))

for i in range(rows):
    matrix[i][n-1] *= 2 

# Вывод результатов
print('Вывод полученной матрицы:')
for i in matrix:
    print(*i, sep='\t')