
""" __iter__() which should return the object itself and which is invoked once
    (it's needed for Python to successfully start the iteration)

    __next__() which is intended to return the next value (first, second, and so on) of the
    desired series - it will be invoked by the for/in statements in order to pass through the
    next iteration; if there are no more values to provide, the method should raise the StopIteration exception."""


class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__p1 = self.__p2 = 1
        self.__i = 0
        self.__n = nn

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)

# ---------------------------------------------------------------------------------------------------------------------


class Fib:
    def __init__(self, nn):
        self.__p1 = self.__p2 = 1
        self.__n = nn
        self.__i = 0

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        return self.__iter


object = Class(8)
for i in object:
    print(i)
