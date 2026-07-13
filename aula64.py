"""
Retorno de valores das funções (return)
"""
variavel = print('Wellison')
# Como print() não tem return próprio, o Python retorna automaticamente: None
print(variavel) # print não devolve um valor útil, ele apenas mostra algo no terminal


# O correto seria guardar a string numa variavel e executar a string.
variavel = 'Wellison'
print(variavel)



# Ou com funções:
def nome():
    return 'Wellison'
variavel = nome()
print(variavel)
