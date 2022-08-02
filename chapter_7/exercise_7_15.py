def input_orders(n):
    """n개의 음료를 주문받아 리스트로 반환한다."""
    return (input() for _ in range(n))  # return [input() for _ in range(n)]


for drink in input_orders(3):
    print(drink, '만들어 주세요!')