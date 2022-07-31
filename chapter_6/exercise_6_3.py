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

    number_of_days_per_month = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if is_leap_year(year):
        number_of_days_feb = 29
    else:
        number_of_days_feb = 28
    number_of_days_per_month.update({2: number_of_days_feb})

    return number_of_days_per_month.get(month)


print(days_in_month(2022, 2))
print(days_in_month(2000, 10))
print(days_in_month(1996, 2))
print(days_in_month(1998, 1))

# 그달이 며칠까지 있는지를 사전으로 저장해 놨었는데요. 2월은 알 수 없으니 2월을 제외한 달을 완성하고, 마지막에 2월을 추가하는 방법을 썼는데...
# 맨 처음 사전은 2월이 없는 미완성 형태라 이런 방법을 쓰는 건 좋지 않은 거 같네요.
