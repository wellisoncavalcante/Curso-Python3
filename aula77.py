# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - Não tem índices;
# - Não garantem ordem;
# - São iteráveis (for, in, not in)

# s1 = {1, 2, 3, 3, 3, 3, 2, 1, 2, 3} # set retira os valores duplicados de iteráveis
# print(s1)

# Consigo também retirar os duplicados de uma lista, por exemplo:
# lista_1 = [1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1] # lista com valores duplicados
# set_1 = set(lista_1) # transforma a lista_1 em set
# lista_2 = list(set_1) # transforma o set_1 em list
# print(lista_2) # lista sem os valores duplicados

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 2, 1}

# print(3 not in s1)
# print(2 in s1)
for numero in s1:
    print(numero)