"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# for letra in texto
texto = 'Wellison' # iteravel
iteratador = iter(texto) #iterator

print('*'*100)
print('como o for funciona')

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

print('*'*100)
print('utilizando o for')
for letra in texto:
    print(letra)