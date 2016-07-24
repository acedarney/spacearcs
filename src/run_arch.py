# graph = Graph('lunar')


class Foo:
    pass


foo = Foo()
names = ['a', 'b', 'c']
for attrs in names:
    setattr(foo, attrs, 10)
foo.d = foo.a + foo.b + foo.c

print(vars(foo))
