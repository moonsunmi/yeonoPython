def print_absolute():
    """사용자로부터 정수를 입력받아 그 수의 절댓값을 화면에 출력한다."""
    print('정수를 입력하세요.')
    number = int(input())
    result = abs(number)
    print(number, '의 절댓값:', result)


print_absolute()