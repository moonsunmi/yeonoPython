def 첫_짝수_찾기(numbers):
    """numbers에서 첫 번째 짝수를 찾아 화면에 출력한다."""
    for n in numbers:
        if n % 2 == 0:
            print(n, '이 첫 짝수입니다.')
            break
    else:
        print('짝수가 없습니다.')

첫_짝수_찾기([1, 3, 5, 33, 47, 55])
첫_짝수_찾기([7, 5, 6, 72, 19, 81])