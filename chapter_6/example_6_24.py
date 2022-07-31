total = 0

for n in range(1, 10_000_001):
    if n % 2 == 0:
        total += n

print(total)
