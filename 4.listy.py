listaObecnosci = [
    'iksiński',  # 0
    'kowalski',  # 1
    'zimny',  # 2
    'świtaj'  # 3
]

print(listaObecnosci[3])

listaObecnosci.append('aniserowicz')

print(listaObecnosci)

listaObecnosci.insert(0, 'dziekan')
print('z dziekanen:')
print(listaObecnosci)

listaObecnosci.extend(['a', 'b', 'c'])
print(listaObecnosci)
