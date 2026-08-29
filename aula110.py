# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Wellison', 'José', 'Ruan', 'Mario',
]

camisetas = [
    ['preta', 'azul', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unissex'],
    ['algodão', 'poliéster', 'linho'],
]

# print('combinação')
# print_iter(combinations(pessoas, 2))

# print('permutação')
# print_iter(permutations(pessoas, 2))

print('product')
print_iter(product(*camisetas))