# 오류 발생 코드
class Cake:
    """케이크를 나타낸는 클래스"""
    coat = '생크림'

    def describe():
        """이 케이크에 관한 정보를 화면에 출력한다."""
        print('이 케이크는', Cake.coat, '으로 덮여 있다.')


cake_1 =Cake()
cake_1.coat = '초콜릿'
cake_1.describe()
