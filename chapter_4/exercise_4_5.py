order_memo = """주문1: 아메리카노
주문2: 카페라테
주문3: 아메리카노, 아메리카노
주문4: 아메리카노, 카페라테
주문5: 카페라테, 카페라테
"""

print("주문:", order_memo.count("주문"))
print("아메리카노:", order_memo.count("아메리카노"))
print("카페라테:", order_memo.count("카페라테"))
