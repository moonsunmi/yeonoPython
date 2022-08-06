def 삼육구(n):
    """n에 숫자 '3', '6', '9' 중 하나 이상이 있을 경우 '짝'을,
    그렇지 않으면 n에 대응하는 숫자를 반환한다."""
    characters = str(n)
    found_3 = characters.find('3') != -1
    found_6 = characters.find('6') != -1
    found_9 = characters.find('9') != -1
    if found_3 or found_6 or found_9:
        return '짝'
    else:
        return str(n)


def test_삼육구():
    if not 삼육구(0) == '0':
        return False

    if not 삼육구(8) == '8':
        return False

    if not 삼육구(3) == '짝':
        return False

    if not 삼육구(6) == '짝':
        return False

    if not 삼육구(9) == '짝':
        return False

    if not 삼육구(120) == '120':
        return False

    if not 삼육구(300) == '짝':
        return False

    if not 삼육구(66669333) == '짝':
        return False

    if not 삼육구(2481112) == '2481112':
        return False

    if not 삼육구(-10) == '-10':
        return False

    if not 삼육구(-9) == '짝':
        return False

    return True


print(test_삼육구())