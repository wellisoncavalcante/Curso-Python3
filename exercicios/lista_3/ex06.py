# Conte quantos números entre 1 e 100 são divisíveis por 3.

i = 1
contador = 0

while i <= 100:
    if i % 3 == 0:
        contador += 1
    i += 1

print(contador)

contador = 0

for i in range(1, 101):
    if i % 3 == 0:
        contador += 1

print(contador)