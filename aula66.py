"""
Exercício com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função fala se é um número par ou ímpar.
Retorne se o número é par ou ímpar
"""

def multiplicao(*args):
    total = 1   # importante.
    for numero in args:
        total = numero * total
    return total

multiplicao_1_2_3 = multiplicao(1, 2, 3, 4, 5)
print(multiplicao_1_2_3)

#   total = 1,  numero = 1      # 1
#   total = 1,  numero = 2      # 2
#   total = 2,  numero = 3      # 6
#   total = 6,  numero = 4      # 24
#   total = 24, numero = 5      # 120

def impar_ou_par(x):
    if x % 2 == 0:
        return('Esse número é par.')
    else:
        return('Esse número é ímpar.')

print(impar_ou_par(3))