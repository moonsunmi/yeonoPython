class Shape:
    """도형을 나타내는 클래스"""

    def describe(self):
        """도형의 특징을 화면에 출력한다. 변의 개수는 self.sides 속성을 읽어 구한다."""
        print('이 도형은', self.sides, '개의 변을 가지고 있습니다.')


class Triangle(Shape):
    """삼각형을 나타내는 클래스"""
    sides = 3

class Rectangle(Shape):
    """사각형을 나타내는 클래스"""
    sides = 4


shapes = [
    Triangle(),
    Rectangle(),
    ]
for shape in shapes:
    shape.describe()
