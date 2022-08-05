# 연습문제 8-13을 모범답안에 가깝게 수정한 것
# Food 메서드를 구현할 때, 사용할 수 있는 메서드를 좀 더 이용함.
class Food:
    """음식을 나타내는 클래스"""
    def __init__(self, taste, calorie):
        """인스턴스를 초기화한다."""
        self._taste = taste
        self._calorie = calorie

    def __str__(self):
        """음식을 표현하는 문자열을 반환한다"""
        return str(self._taste) + '만큼 맛있고 ' + str(self._calorie) + '만큼 든든한 음식'

    def __add__(self, other):
        """다른 음식을 더해 새 음식을 반환한다."""
        taste = self._taste + other._taste
        calorie = self._calorie + other._calorie
        return Food(taste, calorie)

    """ 맛이 좋으면 더 큰것, 같은 맛일 때는 칼로리가 적은 게 큰 것"""

    def __eq__(self, other):  # self == other
        return self._taste == other._taste and self._calorie == other._calorie

    def __lt__(self, other):  # self < other
        if self._taste < other._taste:
            return True
        elif self._taste == other._taste:
            if self._calorie > other._calorie:
                return True
        return False

    def __gt__(self, other):  # self > other
        return other < self

    def __le__(self, other):  # self <= other
        return self < other or self == other

    def __ge__(self, other):  # self >= other
        return other <= self

    def __ne__(self, other):  # self != other
        return not self == other


strawberry = Food(9, 32)
potato = Food(6, 66)
sweet_potato = Food(12, 131)
pizza = Food(13, 266)
print('딸기 < 감자: ', strawberry < potato)
print('감자 + 감자 < 고구마: ', potato + potato < sweet_potato)
print('피자 >= 딸기: ', pizza >= strawberry)
print('피자 >= 피자: ', pizza >= pizza)
print('감자 + 딸기 < 피자: ', potato + strawberry < pizza)
print('딸기 == 딸기: ', potato == potato)


# 메서드를 만든 순간부터, 다른 메서드에서도 활용할 수 있을지 계속 생각해야 겠다.