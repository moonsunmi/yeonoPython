def gap(*args):
    """여러 개의 수를 전달받아, 인자 중 가장 큰 수와 가장 작은 수의 차이를 반환한다."""

    return max(args) - min(args)


print(gap(100))
print(gap(10, 20, 30, 40))
ages = [19, 16, 24, 19, 23]
print(gap(*ages))