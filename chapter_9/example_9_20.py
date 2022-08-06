while True:
    print('0이 아닌 정수를 입력해 주세요:', end=' ')
    user_string = input()

    if not user_string.isnumeric():
        print(user_string, '은 정수가 아닙니다.')
        continue

    user_number = int(user_string)

    if user_number == 0:
        print('0으로 나눌 수 없습니다.')
        continue

    break

print( 1 / user_number)

