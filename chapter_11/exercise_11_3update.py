# 논리 오류: 윤년을 생각 못하고, 1년을 365일로 고정하여 계산함.

from datetime import date, timedelta


class BirthdayException(Exception):
    """생일 오류"""
    pass


def counting_age(birth_date):
    """생년월일(birth_date)을 입력받아 세는 나이를 반환한다."""
    # 세는 나이는 year 계산
    year_gap = date.today().year - birth_date.year
    if year_gap < 0:
        raise BirthdayException('미래에 태어날 사람의 나이는 계산할 수 없습니다.')
    return year_gap + 1


def full_age(birth_date):
    """생년월일(birth_date)을 입력받아 만 나이를 반환한다."""
    # 만 나이는 day 계산
    day_gap = date.today() - birth_date

    if day_gap.days < 0:
        raise BirthdayException('미래에 태어날 사람의 나이는 계산할 수 없습니다.')

    is_after_birthday = timedelta(0) <= date.today() - date(date.today().year, birth_date.month, birth_date.day)

    return date.today().year - birth_date.year + (0 if is_after_birthday else -1)


def test_full_age():

    assert full_age(date(1999, 1, 1)) == 23
    assert full_age(date(1999, 8, 8)) == 22
    assert full_age(date(2000, 1, 1)) == 22
    assert full_age(date(2000, 8, 8)) == 21

    assert full_age(date(2020, 1, 1)) == 2
    assert full_age(date(2020, 12, 31)) == 1
    assert full_age(date(2022, 8, 7)) == 0


def test_counting_age():
    assert counting_age(date(2022, 8, 7)) == 1
    assert counting_age(date(2020, 1, 1)) == 3
    assert counting_age(date(2020, 12, 31)) == 3

    assert counting_age(date(1999, 1, 1)) == 24
    assert counting_age(date(1999, 8, 8)) == 24
    assert counting_age(date(2000, 1, 1)) == 23
    assert counting_age(date(2000, 8, 8)) == 23


test_full_age()
test_counting_age()
try:
    print('만 나이: ', full_age(date(1985, 7, 16)))
except Exception as error:
    print(error)

try:
    print('세는 나이: ', counting_age(date(1985, 7, 16)))
except Exception as error:
    print(error)

try:
    print('만 나이: ', full_age(date(2985, 7, 16)))
except Exception as error:
    print(error)

try:
    print('세는 나이: ', counting_age(date(2985, 7, 16)))
except Exception as error:
    print(error)
