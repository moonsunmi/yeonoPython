식재료별_칼로리 = {
    '밀가루': 364 / 100,
    '피망': 20.1 / 100,
    '올리브': 115 / 100,
    '돼지고기': 242.1 / 100,
}

def 칼로리(food_name, weight):
    """음식의 종류(food_name)와 섭취량(weight)을 매개변수에 전달받아 총 칼로리를 반환한다."""

    return 식재료별_칼로리.get(food_name, 0) * weight


식재료별_칼로리['치즈'] = 402.5 / 100
print(칼로리('치즈', 100))

