def plus_elements(seq1, seq2):
    """두 개의 시퀀스를 전달받은 후 각 요소를 순서대로 합한 리스트를 반환한다.
    ex) (1 , 2, 3) [4, 5, 6]   =>    [5, 7, 9] """

    result_list = []
    for number1, number2 in zip(seq1, seq2):
        result_list.append(number1 + number2)

    return result_list


print(plus_elements((1, 2, 3), [4, 5, 6]))