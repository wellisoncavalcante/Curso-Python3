# Criando arquivos com Python
# Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (criação), a (escreve ao final), b (binário), t (modo texto), 
# + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulos os, mas: 
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera arquivo json
# json.load = lê o arquivo json

caminho_arquivo = 'aula117.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá, mundo!')
    print('O arquivo vai ser fechado automaticamente após o bloco with')