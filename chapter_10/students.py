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


# 기말고사 성적
scores = [99, 98, 96, 100, 99, 92, 93, 27, 96, 85, 100, 99]
# 학생들의 키
heights = [155.8, 182.7, 166.3, 181.1, 179.5, 173.2, 174.5, 162.3]
# 칭찬 도장을 받은 학생
compliments = ['박연오', '김파이', '김파이', '박연오', '박연오']

print('기말고사 성적 평균:', mean(scores))
print('가운데 앉은 학생의 키:', median(heights))
print('칭찬을 가장 많이 받은 학생:', most_frequent(compliments))
