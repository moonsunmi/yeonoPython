i = 0
while(i < 100):
    print(i, '번째 실행')
    i += 1
    if (i > 2):
        print('반복 중지')
        break
else:
    print('반복 완료')