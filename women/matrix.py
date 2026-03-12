n = int(input()) #-количество строк
m = int(input()) # количество столбцов
matrix=[]
# for r in range(n):
#     temp =[]
#     for c in range(m):
#         temp.append(input())
#     matrix.append(temp)

# for item in matrix:
#     print(item)
    
matrix=([input() for c in range(m)] for r in range(n))
for row in matrix:
    print(row)
    
