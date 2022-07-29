def order():
    """사용자로부터 음료를 입력 받아, 주문 내역을 출력한다."""
    print('주문하실 음료를 알려 주세요.')
    drink = input()
    print(drink, '주문하셨습니다.')

order()

print(help(order))