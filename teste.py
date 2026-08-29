def decorador(funcao):
    def interna():
        print('Antes da função')

        funcao()

        print('Depois da função')
    return interna

def saudacao():
    print('Olá!')

# saudacao = decorador(saudacao)
# saudacao()

saudacao = decorador(saudacao)
saudacao()