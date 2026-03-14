n = int(input())
m = int(input())

matrix = [[input() for _ in range(m)] for _ in range(n)]

# Вывод исходной матрицы
for row in matrix:
    print(*row)

print()

# Вывод транспонированной матрицы
for i in range(m):
    print(*[matrix[j][i] for j in range(n)])