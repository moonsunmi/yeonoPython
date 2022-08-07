print('당신의 이름은 무엇인가요?')
name = input()

with open('hello.txt', 'w') as file:
    print(name, '님 반가워요.', file=file)