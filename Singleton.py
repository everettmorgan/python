# inherit metaclass properties from `type`
class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            # instance = type(cls).__call__(cls, *args, **kwargs)
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]


class Foo(metaclass=Singleton):
    # __metaclass__ = Singleton # for python2

    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    a = Foo(1)
    b = Foo(2)
    c = Foo(3)

    print(hex(id(a)), hex(id(b)), hex(id(b)))
