try:
    print('0이 아닌 정수를 입력해 주세요:', end=' ')
    user_number = int(input())
    print(1 / user_number)

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except ValueError:
    print('입력한 값은 정수가 아닙니다.')

