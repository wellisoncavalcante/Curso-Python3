# Exercícios
import copy
from pprint import pprint

def separador():
    print('='*100)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)

# Aumente os preços dos produtos a seguir em 10 %
for i in novos_produtos:
    i['preco'] = round(i['preco'] * 1.1, 2)
pprint(novos_produtos)
separador()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda produto: produto['nome'])
pprint(produtos_ordenados_por_nome)
separador()

# Ordene os produtos por nome decrescente
produtos_ordenados_por_nome_decrescente = copy.deepcopy(produtos)
produtos_ordenados_por_nome_decrescente.sort(key=lambda produto: produto['nome'], reverse=True)
pprint(produtos_ordenados_por_nome_decrescente)
separador()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(produtos)

# Ordene os produtos por preço crescente
produtos_ordenados_por_preco.sort(key=lambda produto: produto['preco'])
pprint(produtos_ordenados_por_preco)
separador()

# Lista original continua intacta
pprint(produtos)