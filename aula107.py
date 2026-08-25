# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Ubatuba', 'Salvador', 'Belo Horizonte', 'Copacabana']
siglas = ['SP', 'BA', 'MG', 'RJ']

resultado = zip(cidades, siglas)

for item in resultado:
    print(item)


# Outra solução sem zip

# cidades_estados = {
#     'Salvador': 'BA',
#     'Ubatuba': 'SP',
#     'Belo Horizonte': 'MG',
#     'Copacabana': 'RJ'
# }

# for cidade in cidades:
#     print(cidade, cidades_estados[cidade])