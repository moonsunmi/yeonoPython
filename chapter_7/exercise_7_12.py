def faulty_rate(diameters):
    # 정상: 지름 0.99mm 이상, 1.01mm 미만

    working_diameters = list(filter(lambda diameter: 0.99 <= diameter < 1.01, diameters))
    return (len(diameters) - len(working_diameters)) / len(diameters)


diameters = [0.985, 0.992, 1.004, 0.995, 0.899, 1.001, 1.002, 1.003, 1.009, 0.998]
print(faulty_rate(diameters))

# 람다식에서 not을 이용하면 더 간단하게 구현할 수 있다.
# lambda diameter: not (0.99 <= diameter < 1.01)