# 오류가 발생하는 예제
import math

coordinate_2 = (3, 5)
triangle_2 = ((0, 0), (0, 3), (4, 3))
rectangle_2 = {
    'point': (2, 2),
    'width': 4,
    'height': 4,
}


def square(x):
    """전달받은 수의 제곱을 반환한다."""
    return x * x


def distance(point_a, point_b):
    return math.sqrt(square(point_a['x'] - point_b['x']) + square(point_a['y'] - point_b['y']))


def circumference_of_triangle(shape):
    """삼각형 데이터를 전달받아 둘레를 구해 반환한다."""
    a_to_b = distance(shape['point_a'], shape['point_b'])
    b_to_c = distance(shape['point_b'], shape['point_c'])
    c_to_a = distance(shape['point_c'], shape['point_a'])

    return a_to_b + b_to_c + c_to_a


print(circumference_of_triangle(triangle_2))


