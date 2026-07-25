# Métodos úteis dos dicionários em Python
# len - Quantas chaves
# keys - Iterável com as chaves
# values - Iterável com os valores
# items - Iterável com chaves e valores
# setdefault - Adiciona valor se a chave não existe
# copy - Retorna uma cópia rasa (shallow copy)
# get - Obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'nome': 'Wellison',
    'sobrenome': 'Cavalcante',
    'idade': 22,
}

d2 = d1
# d1 e d2 referenciam o mesmo dicionário
# nenhuma cópia foi criada.
# portanto, tudo que eu alterar em d2, vai alterar em d1.

d2['nome'] =  'Sara'
# se eu alterar 'nome' do dicionário, ele vai mudar o nome para 'Sara', mas também irá alterar o nome de d1.
# não apenas de d2.

print(d1) # {'nome': 'Sara', 'sobrenome:' 'Cavalcante', 'idade': 22}
print(d2) # {'nome': 'Sara', 'sobrenome:' 'Cavalcante', 'idade': 22}

# Agora vamos utilizar o copy().

print('='*100)

d3 = {
    'nome': 'Wellison',
    'sobrenome': 'Cavalcante',
    'idade': 22,
    'lista': ['maçã', 'banana', 'uva', 'kiwi'],
}

# d4 = d3.copy() # testar utilizando apenas copy.
d4 = copy.deepcopy(d3) # testar utilizando o deepcopy do import copy

# d4 fez uma cópia do dicionário de d3, então foi criado uma cópia, portanto, consigo alterar apenas d3.
# mas é uma cópia rasa, se eu tiver um valor mutável, por exemplo, uma lista, ele não vai fazer uma cópia
# ele vai fazer com que aponte para o mesmo dicionário

d3['nome'] = 'Ótavio'
print(d3)
print(d4)

print('='*100)

d3['lista'][0] = ['laranja']
# Aqui ele não irá alterar apenas o índice 0 da lista de d3, mas também a de d4.

print(d3)
print(d4)

# Para resolver esse problema, podemos utilizar o import copy, junto com 
# copy.deepcopy()
# por exemplo:
# d4 = copy.deepcopy(d3)
