class Cake:
    """케이크를 나타내는 클래스"""

    coat = '생크림'

cake_1 = Cake()
cake_2 = Cake()


Cake.coat = '초콜릿'
Cake.price = 4000
print(Cake.coat)
print(Cake.price)

print(cake_1.coat)
print(cake_1.price)

cake_3 = Cake()
print(cake_3.coat)
print(cake_3.price)