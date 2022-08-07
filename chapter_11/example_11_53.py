try:
    with open('once.text', 'x') as file:
        file.write('이 파일은 한 번만 작성됩니다.')
except FileExistsError:
    print('파일이 이미 존재합니다.')
