class Cake:
    """케이크를 나타내는 클래스"""
    coat = '생크림'

    def __init__(self, topping, price, candles=0):
        """인스턴스를 초기화한다."""
        self.topping = topping
        self.price = price
        self.candles = candles

    def describe(self):
        """케이크에 관한 정보를 화면에 출력한다."""
        print('이 케이크는', self.coat, '으로 덮여 있다.')
        print(self.topping, '을 올려 장식했다.')
        print('가격은', self.price, '원이다.')
        print('초가', self.candles, '개 꽂혀 있다.')


class ChocolateCake(Cake):
    coat = '초콜릿'
    cacao_percent = 32.0


class IceCreamCake(Cake):
    """아이스크림 케이크를 나타내는 클래스"""

    coat = '아이스크림'
    flavor = '정해지지 않은 맛'

    def __init__(self, flavor, topping, price, candles=0):
        self.flavor = flavor
        super().__init__(topping, price, candles)


class FruitIceCreamCake(IceCreamCake):
    """과일 아이스크림 케이크를 나타내는 클래스"""
    def __init__(self, fruit_percent, flavor, topping, price, candles=0):
        self.fruit_percent = fruit_percent
        super().__init__(flavor, topping, price, candles)


Cake.radius = 20
print(IceCreamCake.radius)

IceCreamCake.radius = 16
print(Cake.radius)
print(IceCreamCake.radius)

IceCreamCake.temperature = -1
print(FruitIceCreamCake.temperature)
print(Cake.temperature)