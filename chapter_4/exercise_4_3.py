def almost_equal(x, y, marin_of_error=0.0001):
    """두 실수(x, y)의 차이가 오차허용범위(margin_of_error)를 넘지 않는지 확인한다."""
    gap = x - y
    return abs(gap) < marin_of_error

print(almost_equal(0.0001, 0.00001))
print(almost_equal(0.0001, 0.00001, marin_of_error=0.00001))
