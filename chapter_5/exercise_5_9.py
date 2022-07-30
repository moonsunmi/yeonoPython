def reverse(sequence):
    """시퀀스(sequence)를 입력받아 반대 순서로 뒤집어 반환한다."""
    return sequence[::-1]


print(reverse([10, 20, 30, 40]))
print(reverse(tuple('일월화수목금토')))
print(reverse(range(10)))
print(reverse('파이썬프로그래밍'))

# 슬라이싱 연산 자꾸 쓰는 거 같아서 뭔가 자신 없었지만 모범 답안과 일치함.
