# Funções recursivas e recursividade
# - Funções que podem se chamar de volta
# - Úteis para dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - Fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

n = int(input('Informe um número para calcular o fibonacci e o fatorial: '))
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fibonacci(n))
print(fatorial(n))