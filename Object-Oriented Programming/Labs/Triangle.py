import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"{self.__x}, {self.__y}"


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__a = math.hypot(abs(vertice2._Point__x - vertice1._Point__x), abs(vertice2._Point__y - vertice1._Point__y))
        self.__b = math.hypot(abs(vertice3._Point__x - vertice1._Point__x), abs(vertice3._Point__y - vertice1._Point__x))
        self.__c = math.hypot(abs(vertice2._Point__x - vertice3._Point__x), abs(vertice2._Point__y - vertice3._Point__y))

    def __str__(self):
        return f"{self.__a} {self.__b} {self.__c}"

    def perimeter(self):
        return self.__a + self.__b + self.__c


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
