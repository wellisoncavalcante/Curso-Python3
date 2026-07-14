"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4 # tupla
#print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

#   total = 0, numero = 1       # 1
#   total = 1, numero = 2       # 2
#   total = 3, numero = 3       # 3
#   total = 6                   # 4

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)
# total = 0, numero = 4     # 1
# total = 4, numero = 5     # 2
# total = 9, numero = 6     # 3
# total = 15

print(sum((1, 2, 3)))
print(sum((4, 5, 6)))