# 오류 나는 코드
class Cake:
    """케이크를 나타내는 클래스"""

    coat = '생크림'

cake_1 = Cake()
cake_2 = Cake()

cake_1.topping = '블루베리'
print(cake_1.topping)

print(Cake.topping)

print(cake_2.topping)

