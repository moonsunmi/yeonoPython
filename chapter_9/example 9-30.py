def a(x):
    return 8 / x

def b(y):
    return a(y - 1)

def c(z):
    return b(z - 2)

def d():
    try:
        print('정수를 입력해 주세요:', end='')
        print(c(int(input())))
    except ZeroDivisionError:
        print('0으로는 나눌 수 없습니다.')


d()