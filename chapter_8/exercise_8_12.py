import random
class Dice:
    """다면체 주사위"""
    def __init__(self, sides):
        self._sides = sides
        self._face = random.randint(1, sides)  # <<== 잘못된 곳

    def top(self):
        """현재 나온 면을 반환한다."""
        return self._face

    def roll(self):
        """나온 면을 새 임의 값으로 설정하고 반환한다."""
        self._face = random.randint(1, self._sides)
        return self._face

dice_4 = Dice(4) # 사면체 주사위 생성
print('사면체 주사위 테스트 ----')
print('처음 나온 면:', dice_4.top())
print('다시 굴리기:', dice_4.roll())
print('다시 굴리기:', dice_4.roll())

dice_100 = Dice(100) # 백면체 주사위 생성
print('백면체 주사위 테스트 ----')
print('처음 나온 면:', dice_100.top())
print('다시 굴리기:', dice_100.roll())
print('다시 굴리기:', dice_100.roll())


# 모범답안에서는 _face를 초기화할 때 roll 메서드를 활용했음.
