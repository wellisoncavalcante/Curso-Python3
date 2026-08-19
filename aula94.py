# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

string = 'Wellison' #str
print(isinstance(string, str))

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 10'[1000])
    print('Linha 11')
    c = a / b
    print('Linha 13')
except ZeroDivisionError:
    print('Dividiu por 0')
except NameError:
    print('Nome não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUAR')