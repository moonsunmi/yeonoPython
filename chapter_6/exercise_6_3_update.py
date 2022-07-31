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


def days_in_month(year, month):
    """연도(year)와 월(month)을 입력받아, 그달이 며칠까지 있는지 반환한다."""

    month_have_31_days = {1, 3, 5, 7, 8, 10, 12}
    month_have_30_days = {4, 6, 9, 11}
    month_have_28_or_29_days = {2}


    if month in month_have_31_days:
        return 31
    elif month in month_have_30_days:
        return 30
    else:
       if is_leap_year(year):
           return 29
       else:
           return 28


print('2020년 2월의 날의 수:', days_in_month(2020, 2))
print('2021년 2월의 날의 수:', days_in_month(2021, 2))
print('2021년 5월의 날의 수:', days_in_month(2020, 5))
print('2021년 9월의 날의 수:', days_in_month(2020, 11))


# 모범 답안 방식대로 수정한 버전

