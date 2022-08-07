import re
sample = '1789Pthon박연오fog'
pattern = r'[가-힣]{2,4}'
match = re.search(pattern, sample)
print(match.group())