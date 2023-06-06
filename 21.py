# В матрице найти сумму и произведение элементов строки N (N задать с
# клавиатуры).

from random import randint


rows = randint(3, 6)
columns = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(columns)] for i in range(rows)] # создание матрицы

print('Вывод матрицы:')
for i in matrix:
    print(*i, sep='\t')
    
n = int(input('Введите число N: '))
apl = 1
lst_for_n = []
for j in range(columns):
    lst_for_n.append(matrix[n-1][j])

for _ in lst_for_n:
    apl *= _

# Вывод результатов
print(f'Вывод результата: \nсумма чисел {lst_for_n} равна {sum(lst_for_n)}, их произведение равно {apl}')