"""
키와 몸무게를 입력 받아 비만 정도를 알려준다.

비만도 측정하는 방법:
1. 체질량 지수 = w(체중) / {t(키) * t(키)}
2. 체질량 지수를 이용한 비만 정도 계산법
    체질량 지수 < 18.5   → 저체중
    18.5 <= 체질량 지수 < 23    → 정상
    23 <= 체질량 지수 < 25   → 과체중
    체질량 지수 >= 25     → 비만
"""


def calculate_BMI(t, w):
    return w / (t * t)


def degree_of_obesity(BMI):
    if BMI < 18.5:
        print('저체중입니다.')
    elif BMI < 23:
        print('정상입니다.')
    elif BMI < 25:
        print('과체중입니다.')
    else:
        print('비만입니다.')


print('키를 입력하세요(m): ', end='')
t = float(input())
print('몸무게를 입력하세요(kg): ', end='')
w = float(input())

degree_of_obesity(calculate_BMI(t, w))

