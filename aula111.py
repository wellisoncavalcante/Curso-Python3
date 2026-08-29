# groupy - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Wellison', 'nota': 'A'},
    {'nome': 'Félix', 'nota': 'B'},
    {'nome': 'Renato', 'nota': 'A'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Taryk', 'nota': 'D'},
    {'nome': 'Caua', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Davi', 'nota': 'A'},
    {'nome': 'Daniel', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

# for aluno in alunos_agrupados:
#     print(aluno)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)