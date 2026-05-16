"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropiada.
Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

entrada = input("Informe as horas em número inteiro: ")

try:
    horario = int(entrada)
    if horario >= 0 and horario <=11:
        print(f'Bom dia! Agora são: {horario}')

    elif horario >= 12 and horario <=17:
        print(f'Boa tarde! Agora são: {horario}')

    elif horario >= 18 and horario <=23:
        print(f'Boa noite! Agora são: {horario}')
    
    else:
        print('Não conheço essa hora')
        
except:
    print('Por favor, digite apenas números inteiros')