def n번째_피보나치_수(n):
    """n번째 피보나치 수를 반환한다."""

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return n번째_피보나치_수(n-1) + n번째_피보나치_수(n-2)

for n in range(1, 12):
    print(n번째_피보나치_수(n), end = ' ')