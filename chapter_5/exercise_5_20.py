def concatenate(*text, seperator=''):
    """여러 개의 문자열을 연결해 반환한다"""
    # text = str(text)
    result = seperator.join(text)
    print(result)


concatenate('가난하다고', '해서', '외로움을', '모르겠는가', seperator='/')
concatenate(*'월화수목금토일', seperator=' - ')


# 매개변수 text의 타입이 튜플임. join을 쓰려면 문자열이어야겠다는 생각에 문자열로 바꿨더니, 모든 글자마다 seperator가 들어갔음..
