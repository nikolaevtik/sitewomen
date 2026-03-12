# def stupid_func(phrase: list) -> list:
#     sample = 'Hello Python'
#     return [''.join(char.upper() if char in sample else char for char in word) for word in phrase]


# print(stupid_func(['Pyth','Any','Close']))


# *_, __ = [1,2,3,4]

# a = ++++__*2++-_[0]

# print(a) #чему равно?

# *_, __ = [1,2,3,4]

# a = _ and 0 or __ 

# print(a) #чему равно?
# from operator import itemgetter


# itemgetter
_ = {1, 2, 3}
__ = {3, 2, 1}
print({0}^_^{0})

print({0}|__|{0})


fact = lambda n: 1 if n <= 1 else n * fact(n-1)
print(fact(5))  # 120

# Суммирование через reduce
from functools import reduce
total = reduce(lambda acc, x: acc + x, [1,2,3,4], 0)  # 10


