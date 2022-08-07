import math


def floor_division(dividen, divisor):
    return math.floor(dividen / divisor)


def test_floor_division():
    if not floor_division(3, 2) == 1: # x.5
        return False

    if not floor_division(3, 3) == 1:  # x.5 미만
        return False

    if not floor_division(5, 3) == 1:  # x.5 초과 (무한 소수)
        return False

    if not floor_division(12, 3) == 4:  # x.0
        return False

    return True


print(test_floor_division())

# 모범답안처럼 assert 문을 사용했으면 더 간단하게 했을 텐데!
