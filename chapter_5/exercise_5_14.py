days = {'월', '화', '수', '목', '금', '토', '일'}
working_days = {'월', '화', '수', '목', '금'}
holidays = {'토', '일'}


def is_holiday(day):
    """요일을 입력받아 그 요일이 쉬는 날이면 True, 아니면 False를 반환한다."""

    return day in holidays


print(is_holiday('월'))
print(is_holiday('토'))