# Operadores in e not in
# Strings são iteráveis
#  0  1  2  3  4  5  6  7
#  W  e  l  l  i  s  o  n
# -8 -7 -6 -5 -4 -3 -2 -1

nome = 'Wellison'
print(nome[0])
print(nome[-8])
print('W' in nome)
print('Welli' in nome)

print('='*100)

print('W' not in nome)
print('Welli' not in nome)

print('='*100)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
