def print_price(num_drink):
    """음료의 잔 수(num_drinK)를 전달받아 가격을 화면에 출력한다."""

    price_per_drink = 2500
    total_price = price_per_drink * num_drink

    print('음료', num_drink, '잔:', total_price)


print_price(3)
