# Leia 5 números e calcule a soma deles

# i = 0
# soma = 0

# while i < 5:
#     numero = int(input('Informe um número inteiro qualquer: '))
#     soma += numero
#     i += 1
# print(soma)

soma = 0

for i in range(1, 6):
    numero = int(input('Informe um número inteiro qualquer: '))
    soma += numero
    
print(soma)