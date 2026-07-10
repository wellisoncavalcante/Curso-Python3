"""
Operação ternária (condicional de uma linha)
<valor> if (condição) else <outro valor>
"""

# condicao = 100 == 100;
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

digito = 1 # > 9 == 0; <=9 = digito
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)