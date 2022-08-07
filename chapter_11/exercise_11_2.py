import re


def hangul_only(string):
    pattern = r'[^가-힣]+'
    only_hangul_match = re.split(pattern, string)

    result = ''
    for hangul_word in only_hangul_match:
        result += hangul_word
    return result


print(hangul_only('I like 파이썬 programming.'))
print(hangul_only('a1가b2나c3다d4라e5마f6바g7사'))