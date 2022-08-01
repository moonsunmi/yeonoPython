def longest(*args):
    """여러 개의 시퀀스를 입력받아, 그중 가장 많은 요소를 가진 시퀀스를 반환한다."""

    longest_list = []

    for a_list in args:
        if len(longest_list) < len(a_list):
            longest_list = a_list
    return longest_list


print(longest([1, 2, 3], (4, 5), [], 'abcdefg', range(5)))
print(longest('파이썬', '프로그래밍'))
print(longest(range(10), range(100), range(50)))

# 모범 답안의 다른 예시
# def longest(*sequences):
#     return max(*sequences, key=len)

