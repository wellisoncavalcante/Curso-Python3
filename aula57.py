"""
Lista de listas e seus índices
"""
salas = [
    # 0            #1
    ['Wellison', 'João'],   # 0
        #0
    ['Félix', ],    #1
        #0        #1      #2           #3
    ['Renato', 'Pedro' , 'Caua',],  # 2
]

# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)