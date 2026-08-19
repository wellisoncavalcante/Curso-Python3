# try, except, else e finally
try:
    print('ABRIR O ARQUIVO')
    8/0
except ZeroDivisionError:
    print('Erro: Dividiu por zero')
except IndexError as error:
    print('IndexError')
else:
    print('Não deu erro')
finally:
    print('FECHAR O ARQUIVO')