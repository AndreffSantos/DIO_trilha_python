carros = ('gol')
# carros não é uma tupla
print(isinstance(carros, tuple))

carros = tuple(['gol', 'uno', 'celta'])
# agora carros é uma tupla
print(isinstance(carros, tuple))

# contar quantos elementos tem em uma tupla
print(carros.count('gol'))

# indice de um elemento
print(carros.index('gol'))

# tamnho da tupla
len(carros)
