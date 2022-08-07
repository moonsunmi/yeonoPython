import re
match = re.search('파이썬', '파이썬 프로그래밍')
if match:
    print('문자열에 패턴과 매치하는 텍스트가 존재함:', match.group())
else:
    print('문자열에 패턴과 매치하는 텍스트가 존재하지 않음')

    