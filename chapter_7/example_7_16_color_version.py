board = [
    [['black', '룩'], None, None, None, None, None, None, None],
    [None, None, None, ['black', '킹'], None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, ['white', '비숍'], None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, ['white', '킹'], None, None, None],
]

for row in board:
    for piece in row:
        if piece:
            if piece[0] == 'black':
                print('▲', end=' ')
            else:
                print('△', end=' ')
        else:
            print('.', end=' ')
    print()
