"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver 5 e 6 letras, escreva "Seu nome é normal". Maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Escreva o seu primeiro nome: ')

tamanho_nome = len(nome)
    
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
        
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome tem o tamanho normal')
        
    else:
        print('Seu nome é muito grande')

else:
    print('Digite mais de uma letra!')