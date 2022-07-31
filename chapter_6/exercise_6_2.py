def is_leap_year(this_year):
    """연도(this_year)를 입력받아 그해가 윤년이면 True를 아니면 False를 반환한다."""

    if this_year % 4 == 0:
        if this_year % 400 == 0:
            return True
        elif this_year % 100 == 0:
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


# 윤년 조건에 '100으로 나누어 떨어지면 윤년이 아니다.' '400으로 나누어 떨어지면 윤년이다.'라는 조건이 있다.
# 100을 먼저 물어 보면, 400에서 걸러지기 때문에 400을 먼저 물어보는 식으로 작성했는데... 썩 좋은 방법은 아니었던 것 같다.
# and 연산일 때 if 중첩으로...
