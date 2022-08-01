import pprint
print(sorted([3, -5, 1, -2, -4], key=abs))

items = [
    {'name': '아메리카노', 'price': 2000},
    {'name': '카페라테', 'price': 2500},
    {'name': '카푸치노', 'price': 2400},
]
sorted_items = sorted(items, key=lambda item: item['price'])
pprint.pprint(sorted_items)