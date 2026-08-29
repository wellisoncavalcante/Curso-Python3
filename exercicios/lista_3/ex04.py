# Some todos os números de 0 até n

n = int(input('Informe um número qualquer que irei somar de até o número que você escolher: '))

i = 0
soma = 0

while i <= n:
    soma += i
    i += 1

print(soma)

soma = 0

for i in range(0, n+1):
    soma += i
print(soma)