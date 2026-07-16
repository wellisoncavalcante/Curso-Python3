# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor"
# Chaves podem ser consideradas como "índice" que vimos na lista e podem ser de tipos imutáveis como:
# str, int, float, bool, tuple e etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário
# Usamos as chaves - {} - ou a classe dict para criar dicionários
# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list
pessoa = {
    'nome': 'Wellison',
    'sobrenome': 'Cavalcante',
    'idade': 22,
    'altura': 1.73,
    'endereços': [
        {'rua': 'av brasil', 'numero': 123},
        {'rua': 'av mexico', 'numero': 456},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['sobrenome'])
print(pessoa['endereços'])