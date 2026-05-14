"""
Fatiamento de strings
 0  1  2  3  4  5  6  7  8
 O  l  a     m  u  n  d  o
-9 -8 -7 -6 -5 -4 -3 -2 -1


Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""

print('Olá mundo'[4:])
print('Olá mundo'[4:9])
print('Olá mundo'[:5])

variavel = 'Olá mundo'
print(len(variavel))
print(variavel[-1:-10:-1])
print(variavel[::-1])
