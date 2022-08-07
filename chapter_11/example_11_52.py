from datetime import datetime
now = datetime.now()

text = f'현재 시각: {now.hour:02}:{now.minute:02}:{now.second:02}\n'

with open('time.txt', 'a') as file:
    file.write(text)
