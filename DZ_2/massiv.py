# Создаём матрицу двумерноую 3х3 и заполняем числами от 1-9
matrix = [
    [i for i in range(1, 4)],
    [j for j in range(4, 7)],
    [q for q in range(7, 10)]
]

# Выводим нашу матрицу без [] и без запятых, соединяем " " каждую строку
for row in matrix:
    print('|'.join(str(elem_matrix)for elem_matrix in row))
