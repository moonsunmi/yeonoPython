class FruitJuice():
    """과일 주스"""
    _valid_fruits = {'귤', '복숭아', '청포도', '딸기', '사과'}

    def __init__(self):
        """인스턴스를 초기화한다."""
        self._ingredients = []

    def add_ingredient(self, ingredient):
        """재료(ingredient)를 이 주스에 추가한다."""
        if ingredient in self._valid_fruits:
            self._ingredients.append(ingredient)
        else:
            print(ingredient, '는 과일 주스에 넣을 수 없습니다.', sep='')

    def describe(self):
        """이 주스에 관한 정보를 화면에 출력한다."""
        print('이 주스에는', len(self._ingredients), '개의 재료가 들어 있습니다.')
        print('넣은 재료:', end=' ')
        for ingredient in self._ingredients:
            print(ingredient, end=' ')


juice_1 = FruitJuice()
juice_1.add_ingredient('청포도')
juice_1.add_ingredient('복숭아')
juice_1.add_ingredient('도라지')
juice_1.describe()