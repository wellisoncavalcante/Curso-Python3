# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com as chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# métodos geralmente estão dentro do objeto

pessoa = {
    'nome': 'Wellison',
    'sobrenome': 'Cavalcante',
    'idade': 22,
    'altura': 1.73,
}

# print(len(pessoa))
# print(pessoa.keys())
# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

pessoa.setdefault('idade', None)
print(pessoa['idade'])

# for chave in pessoa:
#     print(chave)

# print('='*100)

# for valor in pessoa.values():
#     print(valor)