# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
# s3 = s1 | s2 # União s1 + s2
# s3 = s1 & s2 # Intersecção apenas o que tem em ambos
# s3 = s1 ^ s2 # Diferença simétrica, itens que não estão nos dois ao mesmo tempo
# s3 = s2 - s1 # Conjunto s2 - s1, retirar de s2 os elementos que estão em s1
# print(s3)