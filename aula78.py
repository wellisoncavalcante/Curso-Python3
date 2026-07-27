# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Wellison')
s1.add(1)
s1.add(2)
s1.update(('Hello, World!', 1, 2, 3, 4))
# s1.clear()
s1.discard('Hello, World!')
s1.discard('Wellison')
print(s1)