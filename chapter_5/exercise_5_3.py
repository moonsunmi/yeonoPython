def mirror(sequence):
    """시퀀스(sequence)를 하나 입력 받아서 그 시퀀스를 뒤집은 시퀀스를 원본에 덧붙여 반환한다.
    단, 원본 시퀀스의 마지막 요소는 덧붙어지 않는다."""
    reversed_sequence = sequence[::-1]
    sequence.pop()
    return sequence + reversed_sequence


print(mirror([1, 2, 3]))
print(mirror(['가', '져', '가', '라']))

# 나는 원본의 마지막 요소를 pop()으로 없애 버렸는데, 모범 답안에서는 마지막 요소 없이 뒤집은 sequence를 구한다.
# reversed_sequence = sequence[-2::-1]. 마지막은 -1이니까, 마지막을 제외하려면 -2.
