class Cake:
    """케이크"""
    coat = '생크림'

class CakePiece:
    """조각케이크"""
    size = 1/ 8
    calorie = 200

class CheeseCake(Cake):
    """치즈케이크"""
    body = '치즈'
    calorie = 1600

class CheeseCakePiece(CakePiece, CheeseCake):
    """치즈 조각 케이크"""
    pass

print('body:', CheeseCakePiece.body)
print('size:', CheeseCakePiece.size)
print('calorie:', CheeseCakePiece.calorie)