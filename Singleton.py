class Singleton:
    instances = {}

    def __new__(cls, clsname, bases, attrs):
        if clsname not in cls.instances:
            cls.instances[clsname] = type(clsname, bases, attrs)
        return cls.instances[clsname]


class Foo(Singleton):
    def __new__(cls, data):
        if cls.__name__ not in cls.instances:
            Singleton.__new__(cls, cls.__name__, (), {'data': data})
        return cls.instances[cls.__name__]


if __name__ == '__main__':
    sa = Foo(1)
    sb = Foo(2)
    sc = Foo(3)

    print(sa.data)
    print(sb.data)
    print(sc.data)

    sa.data = 2

    print(sa.data)
    print(sb.data)
    print(sc.data)

    sb.data = 3

    print(sa.data)
    print(sb.data)
    print(sc.data)

    sa.data = 4

    print(sa.data)
    print(sb.data)
    print(sc.data)
