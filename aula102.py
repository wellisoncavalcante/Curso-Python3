# Exercício - Adiando a execução de funções
import time

def soma (x, y):
    return x + y

def multiplica(x, y):
    time.sleep(5)
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = multiplica(multiplica, 10)