# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Wellison Cavalcante'
pessoa['sobrenome'] = 'Silva'

print(pessoa[chave])

pessoa[chave] = 'João'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome'))    

if pessoa.get('sobrenome') is None:
    print('A chave é NONE')
else:
    print(pessoa['sobrenome'])

# print('ISSO NAO VAI')