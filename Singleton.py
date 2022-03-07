class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Foo(metaclass=Singleton):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    a = Foo(1)
    b = Foo(2)
    c = Foo(3)

    print(hex(id(a)), hex(id(b)), hex(id(b)))
