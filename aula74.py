# Métodos úteis dos dicionários em Python
# len - Quantas chaves
# keys - Iterável com as chaves
# values - Iterável com os valores
# items - Iterável com chaves e valores
# setdefault - Adiciona valor se a chave não existe
# copy - Retorna um cópia rasa (shallow copy)
# get - Obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Wellison',
    'sobrenome': 'Cavalcante',
}
# print(p1.get('nome')) # pega o valor da chave 'nome'

# nome = p1.pop('nome') # Remove a chave 'nome'
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() # Remove a última chave do dicionário
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Wellison novo valor',
#     'idade': 22,
# })
# também pode escrever assim:
# p1.update(nome='Wellison novo valor', idade=22)
# tupla = (('nome', 'Wellison novo valor'), ('idade', 23))
# p1.update(tupla)
lista = [['nome', 'Wellison novo valor'], ['idade', 23]]
p1.update(lista)
print(p1)