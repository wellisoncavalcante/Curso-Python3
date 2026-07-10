"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
     10  9  8  7  6  5  4  3  2  
     7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27  0

Somar todos os resultados: 70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisao da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
    contrário disso:
    resultado é o valor da conta

O primeiro dígito do cpf é 7
"""

cpf = input('Informe o seu CPF! Ex.: 74682489070 ')

if len(cpf) != 11 or not cpf.isdigit():
    print('CPF inválido. Digite exatamente 11 números')
else:
    soma1 = 0
    peso1 = 10

    for digito in cpf[:9]:
        soma1 += int(digito) * peso1
        peso1 -= 1

    resultado1 = (soma1 * 10) % 11
    primeiro_digito = 0 if resultado1 > 9 else resultado1

    cpf_primeiro_digito = cpf[:9] + str(primeiro_digito)

    soma2 = 0
    peso2 = 11

    for digito in cpf_primeiro_digito:
        soma2 += int(digito) * peso2
        peso2 -= 1

    resultado2 = (soma2 * 10) % 11
    segundo_digito = 0 if resultado2 > 9 else resultado2

    print(f'O primeiro dígito: {primeiro_digito}')
    print(f'O segundo dígito: {segundo_digito}')
