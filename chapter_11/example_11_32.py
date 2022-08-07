import re
sample = '이름: 박연오, 연락처: 010-1234-5678, 주소: 부산 어딘가'
pattern = r'01\d-\d{3,4}-\d{4}'
match = re.search(pattern, sample)
print(match.group())