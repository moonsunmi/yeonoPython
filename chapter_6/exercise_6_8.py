def max_in_list(numbers):
    """" 리스트 하나를 매개변수로 전달받아, 리스트에서 가장 큰 요소를 반환한다."""

    max_value = float('-inf')

    for number in numbers:
        if number > max_value:
            max_value = number

    return max_value


print(max_in_list([1, 2, 3]))
print(max_in_list([666, 33, -30, 222]))