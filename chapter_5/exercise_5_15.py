# 3의 배수 또는 4이 배수
multiple_3 = set(list(range(0, 1_000, 3)))
multiple_4 = set(list(range(0, 1_000, 4)))

print(len(multiple_4.union(multiple_3)))
