# Exemplos de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'w' in letras:
        print('VOCÊ ENCONTROU A LETRA PREMIADA!')
        break
    print(letras)