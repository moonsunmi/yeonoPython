"""100 이상, 10,000 미만인 자연수 중에서 5의 배수를 모두 합하면 얼마인지 계산하라."""

n = 100
result = 0

while(n < 10_000):
    result += n
    n += 5

print(result)