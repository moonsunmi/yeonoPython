import random

def infinite_random_number(start, end):

    while True:
        yield random.randint(start, end)


infinite_random_number_generator = infinite_random_number(0, 63)
print(next(infinite_random_number_generator))
print(next(infinite_random_number_generator))
print(next(infinite_random_number_generator))
