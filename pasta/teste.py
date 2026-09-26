def busca_binaria(lista, alvo, inicio, fim, comparacoes=0):
    if inicio > fim:
        return comparacoes
    
    meio = (inicio + fim + 1) // 2
    comparacoes += 1

    if lista[meio] == alvo:
        return comparacoes

    elif alvo < lista[meio]:
        return busca_binaria(lista, alvo, inicio, meio - 1, comparacoes)
    
    return busca_binaria(lista, alvo, meio + 1, fim, comparacoes)

entrada = list(map(int, input().split()))

alvo = entrada[0]
lista = entrada[1:]

print(busca_binaria(lista, alvo, 0, len(lista) - 1))