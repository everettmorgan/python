class Singleton:
    instances = {}

    def __new__(cls, clsname, bases, attrs):
        if clsname not in cls.instances:
            cls.instances[clsname] = type(clsname, bases, attrs or {})
        return cls.instances[clsname]


class Foo(Singleton):
    def __new__(cls, *args):
        return Singleton.__new__(cls, cls.__name__, (), *args)


class Bar(Singleton):
    def __new__(cls, *args):
        return Singleton.__new__(cls, cls.__name__, (), *args)


if __name__ == '__main__':
    sa = Foo({'data': 1})
    sb = Foo({'data': 2})
    sc = Foo({'data': 3})

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

    print('===+++===+++===')

    sd = Bar({'a': 1})
    se = Bar({'a': 2})
    sf = Bar({'a': 3})

    print(sd.a)
    print(se.a)
    print(sf.a)

    sd.a = 10

    print(sd.a)
    print(se.a)
    print(sf.a)

    se.a = 11

    print(sd.a)
    print(se.a)
    print(sf.a)

    sd.a = 12

    print(sd.a)
    print(se.a)
    print(sf.a)
