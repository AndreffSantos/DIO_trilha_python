class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return  self._x or 0

    @x.setter
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = 0

foo= Foo(10)
foo.x = 100
del foo.x
print(foo.x)