class Cake:
    """케이크를 나타내는 클래스"""

    coat = '생크림'

cake_1 = Cake()
cake_2 = Cake()


print(cake_1.coat)
cake_1.coat = '아이스크림'
print(cake_1.coat)
print(Cake.coat)
print(cake_2.coat)