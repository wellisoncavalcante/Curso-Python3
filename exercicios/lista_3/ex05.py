# Faça a tabuada de um número informado pelo usuário.

numero = int(input('Informe um número qualquer: '))

# i = 1

# while i <= 10:
#     print(f'{numero} * {i} = {numero*i}')
#     i += 1

for i in range(1, 11):
    print(f'{numero} * {i} = {numero*i}')