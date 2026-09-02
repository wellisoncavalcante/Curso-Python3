caminho_arquivo = 'C:\\Users\\Wellison\\Desktop\\Curso-Python3\\pasta\\'
caminho_arquivo += 'aula117.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá, mundo!')
    print('O arquivo vai ser fechado automaticamente após o bloco with')
