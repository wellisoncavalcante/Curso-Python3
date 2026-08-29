# count é um iterator sem fim (módulo itertools)
# a diferença é porque um range tem fim

from itertools import count

c1 = count(10, 2)
r1 = range(10, 101, 2)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print('='*100)

print('range')
for i in r1:
    print(i)