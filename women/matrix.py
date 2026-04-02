# n = int(input()) #кол-во строк
# m = int(input()) # кол-во колонок

# matrix = [[int(x) for x in input().split()] for _ in range(n)]

# i,j = int(input()),int(input())

# matrix[j],matrix[i]=matrix[i],matrix[j]
# for _ in matrix:
#     print(_, sep='\n')

import sys

class EmojiNamespace:
    def __init__(self):
        self._funcs = {}
    
    def add(self, emoji, func):
        self._funcs[emoji] = func
        # Пытаемся добавить в глобальную область
        try:
            exec(f"global {emoji}; {emoji} = func", globals(), locals())
        except:
            pass
    
    def __getitem__(self, emoji):
        return self._funcs[emoji]
    
    def __call__(self, emoji, *args, **kwargs):
        return self._funcs[emoji](*args, **kwargs)

# Использование
e = EmojiNamespace()

def smile(player=None):
    if player:
        print(f"Игрок {player} 😊")
    else:
        print("😊")

e.add("😊", smile)

# Вызов разными способами
e["😊"]("Вася")    # Игрок Вася 😊
e("😊")()          # 😊

# Если exec() сработал:
try:
    😊("Вася")
except:
    print("Прямой вызов не поддерживается")




# # # Вывод исходной матрицы
# # for row in matrix
# #     print(*row)

# # print()

# # # Вывод транспонированной матрицы
# # for i in range(m):
# #     print(*[matrix[j][i] for j in range(n)])
# # m = float('-inf')
# l = []
# for i, row in enumerate(matrix):
#     max_val = max(row)
#     l.append((max_val, i, row.index(max_val)))
# max_element = max(l, key=lambda x: x[0])
# print(max_element[1], max_element[2])
