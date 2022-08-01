def length(seq):
    """시퀀스(seq)를 하나 입력 받아 요소의 개수를 반환한다."""

    number = 0
    for _ in seq:
        number += 1

    return number

print(length([1, 2, 3, 4]))