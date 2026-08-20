import importlib

import aula99_m

variavel = 'Wellison'

for i in range(10):
    importlib.reload(aula99_m)

print('Fim')