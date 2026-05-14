"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Wellison'
preco = 100200.123456
variavel = '%s, o preço é de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (15, 15))
