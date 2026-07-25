# Exercício - sistema de perguntas e respostas
import os
import time

acertos = 0
erros = 0

def esperar_e_limpar():
    time.sleep(2)
    os.system('cls')

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '6'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10', '15', '20', '25'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quem é o GOAT?',
        'Opções': ['Wellison', 'Messi', 'Cristiano Ronaldo', 'Fallen'],
        'Resposta': 'Fallen',
    },
]
pergunta_1 = perguntas[0].get('Pergunta')

print(f'Pergunta: {pergunta_1}\n')
print('Opções: ')
print('0) 1')
print('1) 3')
print('2) 4')
print('3) 6')
indice_escolhido = input('Escolha uma opção: ').strip()

while indice_escolhido not in ['0', '1', '2', '3']:
    print('Opção inválida! As opções são apenas 0, 1, 2, 3')
    indice_escolhido = input('Escolha uma opção: ').strip()

opcao_escolhida = perguntas[0]['Opções'][int(indice_escolhido)]
resposta_correta = perguntas[0]['Resposta']

if opcao_escolhida == resposta_correta:
    print('Parabéns! Você escolheu a alternativa correta!')
    acertos +=1
else:
    print('Ops! Resposta incorreta')
    erros +=1
esperar_e_limpar()

pergunta_2 = perguntas[1].get('Pergunta')

print(f'Pergunta: {pergunta_2}\n')
print('Opções: ')
print('0) 10')
print('1) 15')
print('2) 20')
print('3) 25')
indice_escolhido = input('Escolha uma opção: ').strip()

while indice_escolhido not in ['0', '1', '2', '3']:
    print('Opção inválida! As opções são apenas 0, 1, 2, 3')
    indice_escolhido = input('Escolha uma opção: ').strip()

opcao_escolhida = perguntas[1]['Opções'][int(indice_escolhido)]
resposta_correta = perguntas[1]['Resposta']

if opcao_escolhida == resposta_correta:
    print('Parabéns! Você escolheu a alternativa correta!')
    acertos +=1
else:
    print('Ops! Resposta incorreta')
    erros +=1
esperar_e_limpar()

pergunta_3 = perguntas[2].get('Pergunta')

print(f'Pergunta: {pergunta_3}\n')
print('Opções: ')
print('0) Wellison')
print('1) Messi')
print('2) Cristiano Ronaldo')
print('3) Fallen')
indice_escolhido = input('Escolha uma opção: ').strip()

while indice_escolhido not in ['0', '1', '2', '3']:
    print('Opção inválida! As opções são apenas 0, 1, 2, 3')
    indice_escolhido = input('Escolha uma opção: ').strip()

opcao_escolhida = perguntas[2]['Opções'][int(indice_escolhido)]
resposta_correta = perguntas[2]['Resposta']

if opcao_escolhida == resposta_correta:
    print('Parabéns! Você escolheu a alternativa correta!')
    acertos +=1
else:
    print('Ops! Resposta incorreta')
    erros +=1

esperar_e_limpar()

if erros == 0:
    print(f'Você teve um total de {acertos} acertos')
elif erros == 3:
    print(f'Você teve um total de {erros} erros')
else:
    print(f'Você teve um total de {acertos} acertos')
    print(f'Você teve um total de {erros} erros')
input('\nPressione ENTER para encerrar...')
