"""
Higher Order Functions
Funções de primeira classe
"""

# def saudacao(msg):
    # return msg

# saudacao2 = saudacao

# v = saudacao('Bom dia, Wellison!')
# print(v)
# print(saudacao('Bom dia, Coder!\nBoa Tarde, Coder!\nBoa Noite, Coder!\nBoa Madrugada, Coder!\n'))

# ========================================================================================================

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Wellison'))
print(executa(saudacao, 'Boa madrugada', 'Wellison'))