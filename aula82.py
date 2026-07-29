# Função lambda em Python
# A função lambda é uma função como qualquer outra em Python. Porém são funções anônimas que contém apenas uma linha.
# Ou seja, tudo deve ser contido dentro de uma única expressão

lista  = [
    {'nome': 'Wellison', 'sobrenome': 'Cavalcante'},
    {'nome': 'Wallison', 'sobrenome': 'Cavalcante'},
    {'nome': 'Sara', 'sobrenome': 'Silva'},
    {'nome': 'Mirelly', 'sobrenome': 'Franca'},
    {'nome': 'Otavio', 'sobrenome': 'Miranda'},
]

# def ordena(item):
#     return item['sobrenome']

# lista.sort(key=lambda item: item['sobrenome'])

def exibir_dicionario(lista):
    for item in  lista:
        print(item)
    print()

# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])
l3 = sorted(lista, key=lambda item: (item['nome'], item['sobrenome']))

# exibir_dicionario(l1)
# exibir_dicionario(l2)
exibir_dicionario(l3)