# Parametros Positional-Only
def positional_only(a, b, /, c):
    print(f"{a}, {b}, {c}")

# Essas sintaxe vão funcionar.
positional_only("a", "b", "c")
positional_only("a", "b", c="c")

# Essa sintaxe não ira funcionar
positional_only(a="a", b="b", c="c")
