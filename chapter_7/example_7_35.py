coll = [10, 5, 1, 9, 7, 3]

for _ in coll:
    for i in range(len(coll) - 1):
        if coll[i] > coll[i + 1]:
            coll[i], coll[i + 1] = coll[i + 1], coll[i]

print(coll)