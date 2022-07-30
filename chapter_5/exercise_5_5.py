def mean(sequence):
    """시퀀스(sequence) 하나를 입력 받아 시퀀스 내 모든 요소의 산술평균을 반환한다.
    단, 빈 시퀀스는 입력하지 않기로 약속한다."""

    return sum(sequence) / len(sequence)


print(mean([92, -21, 0, 104, 51, 76, -92]))
