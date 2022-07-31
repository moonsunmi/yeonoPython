def price(number):
    """쇼핑몰에서 구매할 상품 개수(number)를 입력받아, 총 지불해야 할 가격을 계산한다."""

    if number < 10:
        return number * 100
    elif number < 30:
        return number * 95
    elif number < 100:
        return number * 90
    else:
        return number * 85


print(price(8))
print(price(12))
print(price(38))
print(price(1000))