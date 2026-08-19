# dir, hasattr e getattr em Python

"""
Anotações:
dir(), hasattr() e getattr() são úteis quando seu programa precisa
descobrir ou acessar atributos/métodos de um objeto dinamicamente, ou
seja, quando você não sabe antecipadamente no código qual atributo
ou método será usado.

hasattr() -> "Esse objeto possui esse atributo ou método?"
print(hasattr(nome, 'upper')) True
print(hasattr(nome, 'lower')) True
print(hasattr(nome, 'banana')) False

getattr() -> Pega o método

dic() -> "O que esse objeto possui?"
print(dic(nome)) -> Mostra os atributos e métodos desse objeto
"""
string = 'Wellison'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)