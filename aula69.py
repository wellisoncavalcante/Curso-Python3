# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro

def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadruplicar(numero):
    return numero * 4

resultado_1 = duplicar(4)
resultado_2 = triplicar(4)
resultado_3 = quadruplicar(4)
print(resultado_1)
print(resultado_2)
print(resultado_3)

# ======================
print('='*100)
# ======================

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(4))
print(triplicar(4))
print(quadruplicar(4))