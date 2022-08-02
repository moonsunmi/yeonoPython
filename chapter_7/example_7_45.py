def one_to_three():
    """1, 2, 3을 반환하는 생성기를 반환한다."""
    yield 1
    yield 2
    yield 3

one_to_three_generator = one_to_three()

print(next(one_to_three_generator))
print(next(one_to_three_generator))
print(next(one_to_three_generator))