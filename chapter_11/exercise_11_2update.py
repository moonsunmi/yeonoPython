import re


def hangul_only(string):
    pattern = r'[^가-힣]+'
    only_hangul = re.sub(pattern, '', string)

    return only_hangul


def test_hangul_only():
    assert hangul_only('') == ''
    assert hangul_only('안녕') == '안녕'
    assert hangul_only('123') == ''
    assert hangul_only('안녕 00 나의 vv 친구')


test_hangul_only()
print(hangul_only('I like 파이썬 programming.'))
print(hangul_only('a1가b2나c3다d4라e5마f6바g7사'))