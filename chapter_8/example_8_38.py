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

cake_1 = Cake('눈사람 사탕', 10000)
cake_2 = Cake('한라봉', 9000, 8)

print('케이크 1:')
cake_1.describe()

print('케이크 2:')
cake_2.describe()