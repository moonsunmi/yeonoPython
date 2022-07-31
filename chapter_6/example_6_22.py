def my_sum(numbers):
    """numbers의 모든 요소의 합을 반환한다."""

    total = 0
    for n in numbers:
        total += n
    return total

print(my_sum([1, 2, 3, 4, 5]))