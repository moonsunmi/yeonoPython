try:
    exception = ZeroDivisionError('0으로 나눌 수 없음')
    exception.user = '박연오'
    raise exception
except ZeroDivisionError as e:
    print('오류원인:', str(e))
    print('오류 일으킨 사용자:', exception.user)