"""
100 이상, 10,000 미만인 자연수 중에서 5의 배수를 모두 합하면 얼마인지 계산하라.
for, range version
"""

result = 0
for n in range(100, 10_000, 5):
    result += n

print(result)
