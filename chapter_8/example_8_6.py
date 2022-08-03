# 유형: '좌표'는 다음 키를 가지는 사전이다.
#   * 'x': x축의 위치 (정수)
#   * 'y': y축의 위치 (정수)
coordinate_1 = {'x': 5, 'y': 3}

# 유형: '삼각형'은 다음 키를 가지는 사전이다.
#   * 'point_a': 첫 번째 점의 위치(좌표)
#   * 'point_b': 두 번째 점의 위치(좌표)
#   * 'point_c': 세 번째 점의 위치(좌표)
triangle_1 = {
    'point_a': {'x': 0, 'y': 0},
    'point_b': {'x': 3, 'y': 0},
    'point_c': {'x': 3, 'y': 4},
}


# 유형: '사각형'은 다음 키를 가지는 사전이다.
#   * 'point_a': 첫 번째 점의 위치(좌표)
#   * 'point_b': 두 번째 점의 위치(좌표)
#   * 'point_c': 세 번째 점의 위치(좌표)
#   * 'point_d': 첫 번째 점의 위치(좌표)
rectangle_1 = {
    'point_a': {'x': 2, 'y': 2},
    'point_b': {'x': 6, 'y': 2},
    'point_c': {'x': 6, 'y': 6},
    'point_d': {'x': 2, 'y': 6},
}

import math


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


def circumference_of_rectangle(shape):
    """사각형 데이터를 전달받아 둘레를 구해 반환한다."""
    a_to_b = distance(shape['point_a'], shape['point_b'])
    b_to_c = distance(shape['point_b'], shape['point_c'])
    c_to_d = distance(shape['point_c'], shape['point_d'])
    d_to_a = distance(shape['point_d'], shape['point_a'])

    return a_to_b + b_to_c + c_to_d + d_to_a


print(circumference_of_triangle(triangle_1))
print(circumference_of_rectangle(rectangle_1))