# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

# print(list(range(10)))

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []

for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [numero * 4 for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'produto_1', 'preço': 19.99},
    {'nome': 'produto_2', 'preço': 24.99},
    {'nome': 'produto_3', 'preço': 5.35},
    {'nome': 'produto_4', 'preço': 6.92},
]

novos_produtos = [
    {**produto, 'preço': round(produto['preço'] * 1.30, 2)}
    if produto['preço'] > 20 else {**produto} # Aumento de 30% se o preço for maior que 20
    for produto in produtos
]
# print(*novos_produtos, sep='\n')
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]

novos_produtos = [
    {**produto, 'preço': round(produto['preço'] * 1.30, 2)}
    if produto['preço'] > 20 else {**produto} # Aumento de 30% se o preço for maior que 20
    for produto in produtos
    if (produto['preço'] > 20 and produto['preço'] * 1.05) > 10
]
p(novos_produtos)