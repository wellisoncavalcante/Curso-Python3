from functools import reduce

def soma(x, y):
    return x + y

lista = [47, 11, 42, 13]

# print(reduce(soma, lista))

print(reduce(lambda x, y: x + y, lista))