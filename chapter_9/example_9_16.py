def frequency(s, c):
    """문자열 s와 문자 c를 입력받아, c가 s에 등장하는 빈도를 구한다.
    테스트:
    * 'banana', 'a' => 0.5
    * 'code', 'c' => 0.25
    * '파이썬', '프' => 0
    * '파이썬', '파이' => None
    * '', 'a' => 0
    """
    if len(c) != 1:
        return None

    if len(s) == 0:
        return 0

    count = s.count(c)
    return count / len(s)


def test_frequency():
    """frequency() 함수 테스트"""
    if not (frequency('banana', 'a') == 0.5):
        return False

    if not(frequency('code', 'c') == 0.25):
        return False

    if not(frequency('파이썬','프') == 0):
        return False

    if not(frequency('파이썬', '파이') == None):
        return False

    if not (frequency('', 'a') == 0):
        return False

    return True


print(test_frequency())
