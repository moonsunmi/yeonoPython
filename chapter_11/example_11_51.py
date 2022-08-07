from datetime import date
today = date.today()

text = f'안녕하세요! 오늘은 {today.month}월 {today.day}일입니다.\n'

with open('hello.txt', 'w') as file:
    file.write(text)
