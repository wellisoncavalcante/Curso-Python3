from sys import path

import aula100_package.modulo
from aula100_package import modulo
from aula100_package.modulo import *
# from aula100_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula100_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(3, 3))
print(variavel)