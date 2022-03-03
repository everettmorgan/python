class Singleton:
    instances = {}

    def __new__(cls, clsname, bases, attrs):
        if clsname not in cls.instances:
            cls.instances[clsname] = type(clsname, bases, attrs)
        return cls.instances[clsname]


class Foo(Singleton):
    def __new__(cls, data):
        if cls.__name__ not in cls.instances:
            Singleton.__new__(cls, cls.__name__, (), {
                'data': data,
            })
        return cls.instances[cls.__name__]


class Bar(Singleton):
    def __new__(cls, data):
        if cls.__name__ not in cls.instances:
            Singleton.__new__(cls, cls.__name__, (), {
                'data': data,
            })
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

    print('===+++===+++===')

    sd = Bar(5)
    se = Bar(6)
    sf = Bar(7)

    print(sd.data)
    print(se.data)
    print(sf.data)

    sd.data = 10

    print(sd.data)
    print(se.data)
    print(sf.data)

    se.data = 11

    print(sd.data)
    print(se.data)
    print(sf.data)

    sd.data = 12

    print(sd.data)
    print(se.data)
    print(sf.data)
