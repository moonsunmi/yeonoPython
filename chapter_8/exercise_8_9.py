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


point_1 = Coordinate(-1, 2)
point_2 = Coordinate(2, 3)

print(point_1.distance(point_2))