# 체스말 데이터 유형 정의하기
#   'x': x축의 위치
#   'y': y축의 위치
#   'color': 체스말의 색깔
#   'role': 체스말의 역할

체스말1 = {'type': '체스말', 'x': 'A', 'y': '8', 'color': 'black', 'role': '룩'}
체스말2 = {'type': '체스말', 'x': 'E', 'y': '1', 'color': 'white', 'role': '킹'}


# 바둑돌 데이터 유형 정의하기
#   'x': x축의 위치
#   'y': y축의 위치
#   'order': 바둑돌이 놓인 수
#   'color': 바둑돌의 색깔

바둑돌1 = {'type': '바둑돌', 'x': 8, 'y': 14, 'order': 83, 'color': '흑'}
바둑돌2 = {'type': '바둑돌', 'x': 12, 'y': 3, 'order': 84, 'color': '백'}


def print_piece(piece):
    """말을 전달받아 종류에 따라 다른 형태로 위치를 출력한다."""

    if piece['type'] == '체스말':
        print(piece['color'] + ' 룩이 ' + piece['x'] + piece['y'] + '위치에 놓여 있어요.')
    elif piece['type'] == '바둑돌':
        print('제 ', piece['order'], ' 수: ', piece['color'], '을 (',
              piece['x'], ', ', piece['y'], ') 위치에 두었습니다.', sep='')


print_piece(체스말1)
print_piece(바둑돌2)
