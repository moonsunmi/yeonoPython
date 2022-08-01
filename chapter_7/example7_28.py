prices = [2500, 3000, 1800, 3500, 2000, 3000, 2500, 2000]
most_expensive = 0

for price in prices:
    if most_expensive < price:
        most_expensive = price

print(most_expensive)