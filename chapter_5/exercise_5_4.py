def minmax(sequence):
    """전달받은 시퀀스(sequence)의 최솟값과 최댓값을 리스트에 담아 반환한다."""

    return [min(sequence), max(sequence)]


print(minmax([92, -21, 0, 104, 51, 76, -92]))
print(minmax(['파', '이', '썬', '프', '로', '그', '래', '밍']))
print(minmax('파이썬프로그래밍'))  # 문자열도 시퀀스