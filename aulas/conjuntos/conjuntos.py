# Conjuntos  são uma coleção que não tem repetições.
a = set([1,2,3,1,3,4])
print(a)

b = set("abacaxi")
print(b)

c = set(("palio", "gol", "celta", "palio"))
print(c)

# Metodos de conjuntos
a = {1, 2, 3}
b = {2, 3, 4}

# União
print(a.union(b))
# Interseção
print(a.intersection(b))
# Diferença
print(a.difference(b))
# Diferença simetrica
print(a.symmetric_difference(b))

# É subconjunto
b = {4, 1, 2, 5, 6, 3}
print(a.issubset(b))

# É disjuntos
a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9}
c = {1, 0}
print(a.isdisjoint(b))

# Adicionar um novo elemento (Se o elemento já existir não fará nada)
d = {1, 23}
print(d)
d.add(25)
print(d)
d.add(42)
print(d)
d.add(25)
print(d)

d.clear()
print(d)

d = c.copy()
print(d)

d.discard(1)
d.discard(10)
print(d)
# A diferença entre discard e remove é que o metodo remove da erro se o elemento não existe no conjunto.

print(a)
a.pop()
print(a)
