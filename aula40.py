"""
Calculadora com while
"""

while True:
    
    numero_1 = input('Informe um número: ')
    numero_2 = input('Informe outro número: ')
    operador = input('Informe um operador ( + - / * ): ')
    
    numeros_validos = None
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue
        
    operador_permitidos = '+-/*'
        
    if operador not in operador_permitidos:
        print('O operador informado é inválido')
        continue
    
    if len(operador) > 1:
        print('Informe apenas um operador')
        continue

    if operador == '+':
        print(f'O resultado é: {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'O resultado é: {num_1_float - num_2_float}')
    elif operador == '/':
        print(f'O resultado é: {num_1_float / num_2_float}')
    elif operador == '*':
        print(f'O resultado é: {num_1_float * num_2_float}')
    else:
        print('Nunca nem deveria ter chegado aqui')
        
    sair = input('Deseja sair? [s]im: e qualquer outra coisa para continuar').lower().startswith('s')
    
    if sair is True:
        break
    
    if sair is False:
        continue 