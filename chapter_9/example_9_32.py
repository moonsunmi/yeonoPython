def get(index_or_key, collection):
    """컬렉션(collection)에서 인덱스 또는 키(index_or_key)에 해당하는 값을 반환한다.
    데이터 집합에 해당하는 인덱스 또는 키가 존재하지 않는 경우 None을 반환한다."""

    try:
        value = collection[index_or_key]
    except (IndexError, KeyError):
        return None
    else:
        return value

print(get(3, (1, 2, 3)))