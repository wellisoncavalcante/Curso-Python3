"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    - append(): Adiciona um item no final da lista
    - pop() - Remove o item no final da lista ou remove um índice
    - insert() - Adiciona um item no índice escolhido
    - del - Apaga um índice
    - clear - Limpa a lista
    - extend - Extende a lista
    - ' + - ' - Concatena listas 
Create Read Update Delete
Criar, Ler, Atualizar, Deletar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]

lista.append(50)  # [10, 20, 30, 40, 50]


lista.pop()  # [10, 20, 30, 40]

del lista[-1]  # [10, 20, 30]

lista.clear()  # [ ]


lista = [10, 20, 30, 40]

lista.insert(0, 5)  # [ 5, 20, 30, 40]

# ['Wellison Cavalcante', 5, 20, 30, 40]
lista.insert(0, 'Wellison Cavalcante')


lista = [10, 20, 30, 40]
# [10, 20, 30, 40, 5] -> Se não existir o índice 100, ele joga para o último elemento da lista.
lista.insert(100, 5)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b  # [1, 2, 3, 4, 5, 6]

lista_d = lista_a.extend(lista_b)  # None

lista_a.extend(lista_b)  # [1, 2, 3, 4, 5, 6]
