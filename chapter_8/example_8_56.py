class Food:
    """음식을 나타내는 클래스"""
    def __init__(self, taste, calorie):
        """인스턴스를 초기화한다."""
        self._taste = taste
        self._calorie = calorie

    def to_string(self):
        """음식을 표현하는 문자열을 반환한다"""
        return str(self._taste) + '만큼 맛있고 ' + str(self._calorie) + '만큼 든든한 음식'

    def add(self, other):
        """다른 음식을 더해 새 음식을 반환한다."""
        taste = self._taste + other._taste
        calorie = self._calorie + other._calorie
        return Food(taste, calorie)

food1 = Food(7, 85)
print(food1.to_string())

food2 = Food(12, 266)
print(food2.to_string())

food3 = food1.add(food2)
print(food3.to_string())