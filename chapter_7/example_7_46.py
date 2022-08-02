def one_to_infinite():
    """ 1부터 무한대 범위의 자연수를 순서대로 내는 생성기를 반환한다."""

    n = 1
    while True:
        yield n
        n += 1

one_to_infinite_generator = one_to_infinite()

print(next(one_to_infinite_generator))
print(next(one_to_infinite_generator))
print(next(one_to_infinite_generator))
print(next(one_to_infinite_generator))
print(next(one_to_infinite_generator))
print(next(one_to_infinite_generator))
