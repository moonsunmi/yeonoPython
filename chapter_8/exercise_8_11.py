import math


def square(x):
    """전달받은 수(x)의 제곱을 반환한다."""
    return x * x


class Coordinate():
    """좌표를 나타낸다."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point_2):
        """두 점 사이의 거리를 계산해 반환한다."""
        return math.sqrt(square(self.x - point_2.x) +
                         square(self.y - point_2.y))


class Shape:
    """도형을 나타내는 클래스"""

    def describe(self):
        """도형의 특징을 화면에 출력한다. 변의 개수는 self.sides 속성을 읽어 구한다."""
        print('이 도형은', self.sides, '개의 변을 가지고 있습니다.')


class Triangle(Shape):
    """삼각형을 나타내는 클래스"""
    sides = 3

    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c


    def circumference(self):
        """도형의 둘레를 계산하여 반환한다."""
        return self.point_a.distance(self.point_b) + self.point_b.distance(self.point_c) + \
                self.point_c.distance(self.point_a)

class Rectangle(Shape):
    """사각형을 나타내는 클래스"""
    sides = 4

    def __init__(self, point_a, point_b, point_c, point_d):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d


    def circumference(self):
        """도형의 둘레를 계산하여 반환한다."""
        return self.point_a.distance(self.point_b) + self.point_b.distance(self.point_c) + \
                self.point_c.distance(self.point_d) + self.point_d.distance(self.point_a)


shapes = [
    Triangle(Coordinate(0, 0), Coordinate(3, 0), Coordinate(3, 4)),
    Rectangle(Coordinate(2, 2), Coordinate(6, 2), Coordinate(6, 6), Coordinate(2, 6))
]
for shape in shapes:
    shape.describe()
    print('둘레:', shape.circumference())
