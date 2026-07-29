# Empacotamento e desempacotamento de dicionários
a, b = 1, 2 # a = 1, b = 2
a, b = b, a # a = 2, b = 1
# print(a, b) # 2, 1

pessoa =  {
    'nome': 'Wellison',
    'sobrenome': 'Cavalcante',
    'idade': 22,
    'Curso': 'Sistemas de Informação',
    'Faculdade': 'UFRPE',
}
# a, b, c, d, e = pessoa.values()
# a, b, c, d, e = pessoa.items()
# print(a, b, c, d, e)

# for valor in pessoa.items():
#     print(valor)

# args e kwargs
# kwargs - keyword argument (argumentos nomeados)

dados_pessoa = {
    'idade': 16,
    'Cidade': 'Recife',
    'Estado': 'Pernambuco',
}

pessoa_dado = {**pessoa, **dados_pessoa}

# print(pessoa_dado)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

# mostro_argumentos_nomeados(1, 2, nome='Wellison', aleatorio=67)
mostro_argumentos_nomeados(**pessoa_dado)