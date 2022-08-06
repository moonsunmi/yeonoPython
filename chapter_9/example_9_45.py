total = 0
file = open('prices.txt')
for line in file:
    total += int(line)
print(total)
file.close()