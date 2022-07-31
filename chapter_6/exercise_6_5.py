def absolute_number(number):
    """수(number)의 절댓값을 구한다. 조건부 식을 활용해서 작성되었음."""

    number = number * -1 if number < 0 else number

    return number


print(absolute_number(-2))
print(absolute_number(3))
print(absolute_number(0))
