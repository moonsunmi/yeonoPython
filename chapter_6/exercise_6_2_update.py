def is_leap_year(this_year):
    """연도(this_year)를 입력받아 그해가 윤년이면 True를 아니면 False를 반환한다."""

    if this_year % 4 == 0:
        if this_year % 100 == 0:
            if this_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print('1996년은 윤년인가?', is_leap_year(1996))
print('1900년은 윤년인가?', is_leap_year(1900))
print('2000년은 윤년인가?', is_leap_year(2000))
print('2020년은 윤년인가?', is_leap_year(2020))
print('2021년은 윤년인가?', is_leap_year(2021))


# 모범답안 방식대로 수정한 버전.
