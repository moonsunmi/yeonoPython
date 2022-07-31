def 절댓값(n):
    """수 n을 입력받아, 절댓값을 반환한다."""
    if n >= 0:
        return n
    if n < 0:
        return -n


print('10의 절댓값:', 절댓값(10))
print('-5의 절댓값:', 절댓값(-5))
