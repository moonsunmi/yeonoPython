def price(num_drink):
    """음료의 잔 수(num_drink)를 전달받아 가격을 반환한다."""
    price_per_drink = 2500
    total_price = price_per_drink * num_drink

    return total_price


result = price(3)
print('가격:', result)