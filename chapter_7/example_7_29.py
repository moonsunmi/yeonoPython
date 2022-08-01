prices = [2500, 3000, 1800, 3500, 2000, 3000, 2500, 2000]
filtered_prices = []

for price in prices:
    if price <= 2000:
        filtered_prices.append(price)

print(filtered_prices)