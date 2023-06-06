# В матрице найти минимальный и максимальные элементы.


from random import randint


rows = randint(3, 6)
colums = randint(3, 6)
matrix = [[randint(-10, 10) for j in range(colums)] for i in range(rows)] #создание матрицы

min_element = min(min(row) for row in matrix)
max_element = max(max(row) for row in matrix)

# Вывод результатов
print("Вывод матрицы:")
for row in matrix:
    print(*row, sep='\t')

print(f"Минимальный элемент: {min_element}")
print(f"Максимальный элемент: {max_element}")
