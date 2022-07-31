def is_prime(number):
    """어떤 수(number)를 입력 받아 그 수가 소수인지를 반환한다. (소수면 True, 아니면 False)"""

    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


sum = 0
for i in range(1, 100):
    if is_prime(i):
        sum += i

print(sum)