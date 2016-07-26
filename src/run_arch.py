# graph = Graph('lunar')


class Foo:
    pass


def create_foo():
    foo = Foo()
    names = ['a', 'b', 'c']
    for attrs in names:
        setattr(foo, attrs, 10)
    foo.d = foo.a + foo.b + foo.c
    return foo

# print(vars(foo))


def test_foo1():
    foo = create_foo()
    assert foo.a == 10


def test_foo2():
    foo = create_foo()
    assert foo.b == 1
