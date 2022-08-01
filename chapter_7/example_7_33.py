coll = [10, 5, 1]

if coll[0] > coll[1]:
    coll[0], coll[1] = coll[1], coll[0]
print(coll)

if coll[1] > coll[2]:
    coll[1], coll[2] = coll[2], coll[1]
print(coll)