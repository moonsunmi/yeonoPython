def abc():
    """a, b, c를 출력하는 생성기를 반환한다."""
    yield 'a'
    yield 'b'
    yield 'c'

abc_generator = abc()

print(next(abc_generator))
print(next(abc_generator))
print(next(abc_generator))
print(next(abc_generator))
print(next(abc_generator))
