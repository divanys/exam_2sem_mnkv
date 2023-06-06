# Если в матрице имеются положительные элементы, то вывести TRUE,
# иначе FALSE.
from random import randint


rows = randint(2, 6)
columns = randint(2, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы
Positive = False

for i in matrix:
    for j in i:
        if j > 0:
            Positive = True
            
print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')


print(Positive)