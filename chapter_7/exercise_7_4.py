happiness = {
    '호주': 7.95,
    '노르웨이': 7.9,
    '미국': 7.85,
    '일본': 6.2,
    '한국': 5.75,
}

for country, happy in happiness.items():
    print(country + ' 사람들은 ' + str(happy) + '만큼 행복합니다.')
# 모범 답안에서는 print할 때 각 요소를 쉼표로 넣고, sep=''로 했음.