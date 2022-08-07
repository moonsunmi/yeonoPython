def mean(seq):
    """시퀀스의 산술평균을 구한다."""
    return sum(seq) / len(seq)


def median(seq):
    """시퀀스의 중앙값을 구한다."""
    n = len(seq)  # 시퀀스의 길이와
    sorted_seq = sorted(seq)  # 정렬된 시퀀스를 구한다.

    # 시퀀스 길이가 짝수인 경우: 가운데 두 원소의 평균을 반환한다.
    if n % 2 == 0:
        return (sorted_seq[n // 2 - 1] + sorted_seq[n // 2]) / 2
    # 그 외: 가운데 원소를 반환한다.
    else:
        return sorted_seq[n // 2]


def most_frequent(seq):
    """시퀀스의 최빈값을 구한다."""
    # 사전에 빈도 기록
    frequencies = {}
    for element in seq:
        if element in frequencies:
            frequencies[element] += 1
    else:
        frequencies[element] = 1

    # 사전의 항목들을 빈도순으로 정렬하고 최빈값을 반환한다.
    frequencies = sorted(frequencies.items(), key=lambda item: item[1])
    return frequencies[-1][0]

