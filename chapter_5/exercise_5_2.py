def center(sequence):
    """시퀀스(sequence)를 하나 입력받아, 그 시퀀스의 가운데 요소를 반환한다."""
    return sequence[int(len(sequence) / 2)]


print(center(['가', '나', '다', '라', '마']))
print(center([2, 4, 8, 16, 32]))

# 나는 중간값을 계산하기 위해서 int(len(sequence) / 2)로 했는데, 모범답안에는 len(sequence) // 2로 되어 있다. 몫 연산자가 쓸데가 별로 없다고 생각했는데.. 이렇게 쓸 수 있구나.
