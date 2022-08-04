class Cake:
    """케이크를 나타낸는 클래스"""
    coat = '생크림'

    def __init__(self, candles):
        """인스턴스를 초기화한다."""
        self.candles = candles

    def describe(self):
        """이 케이크에 관한 정보를 화면에 출력한다."""
        print('이 케이크는', self.coat, '으로 덮여 있다.')
        print('초가', self.candles, '개 꽂혀 있다.')


cake_1 = Cake(12)
cake_2 = Cake(100)

print('케이크 1:')
print('초 개수:', cake_1.candles)

print('케이크 2:')
cake_2.describe()
