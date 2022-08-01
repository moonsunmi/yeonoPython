prices = [2500, 3000, 1800, 3500, 2000, 3000, 2500, 2000]
total_price = 0
num_items = 0

for price in prices:
    total_price += price
    num_items += 1

print(total_price / num_items)
