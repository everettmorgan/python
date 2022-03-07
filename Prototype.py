import time
from abc import abstractmethod


class Prototype:
    @abstractmethod
    def get_clone(self):
        ...


class ExpensiveClass(Prototype):
    def __init__(self, data=None):
        self.data = data

    @staticmethod
    def initialize(data):
        new = ExpensiveClass(data)
        time.sleep(5)
        return new

    def get_clone(self):
        return ExpensiveClass(self.data)


if __name__ == '__main__':
    start = time.time()
    expensive = ExpensiveClass.initialize(5)
    end = time.time() - start
    print('expensive:', end)

    start = time.time()
    cheap = expensive.get_clone()
    end = time.time() - start
    print('cheap:', end)

    # expensive: 5.0034661293029785
    # cheap: 1.0967254638671875e-05
