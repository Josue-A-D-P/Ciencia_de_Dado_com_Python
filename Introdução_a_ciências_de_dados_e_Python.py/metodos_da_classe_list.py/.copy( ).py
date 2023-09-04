lista = [1, 'Python', [50, 80, 10]]

l2 = lista.copy()

print(lista)
print()

print(id(l2), id(lista))
print()

l2[0] = 2

print(f'{lista}\n{l2}')