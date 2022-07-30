# 3과 4의 차집합
multiple_3 = set(list(range(0, 1_000, 3)))
multiple_4 = set(list(range(0, 1_000, 4)))

print(len(multiple_3.difference(multiple_4)))