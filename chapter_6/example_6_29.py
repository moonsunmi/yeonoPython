total = 0

while True:
    print('더할 수를 입력하세요: ', end='')
    user_input = input()

    if user_input == '그만':
        break

    if not user_input.isnumeric():
        print('잘못된 입력입니다.')
        continue

    total += int(user_input)
    print('합계:', total)

print('프로그램을 종료합니다.')