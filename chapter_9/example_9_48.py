with open('prices.txt') as file:
    try:
        total = 0
        file = open('prices.txt')
        for line in file:
            total += int(line)
    except ValueError:
        print('숫자가 아닌 텍스트가 있습니다.')
    else:
        print(total)
