import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista)) # Salva tudo na memória
print(sys.getsizeof(generator)) # Não salva tudo diretamente na memória, vai utilizando de acordo com o que é chamado

print(generator)

# for n in generator:
#     print(n)