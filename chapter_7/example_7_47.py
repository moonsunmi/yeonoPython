def countdown(start, end):
    """start(포함)부터 end(비포함)까지 거꾸로 세는 생성기를 반환한다."""
    n = start
    while end < n:
        yield n
        n -= 1

print(list(countdown(10, 0)))
print(tuple(countdown(100, 95)))

