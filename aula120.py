# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instancias) que podem ter seus próprios atributos e métodos
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações
# Por convenção, usamos PascalCase para nomes de classes
# string = 'Wellison' # str
# print(string.upper())
# print(isinstance(string, str)) # True

class Pessoa:
    ...

p1 = Pessoa() # p1 é uma instância da classe Pessoa
p1.nome = 'Wellison'
p1.sobrenome = 'Cavalcante'

print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
p2.nome = 'Otávio'
p2.sobrenome = 'Miranda'

print(p2.nome)
print(p2.sobrenome)