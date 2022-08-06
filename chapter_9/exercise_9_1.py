def median(data):
    """데이터의 중앙값을 반환한다."""
    sorted_data =sorted(data)
    median_value = sorted_data[int(len(sorted_data) / 2)]
    return median_value

print(median([10, 9, 4, 1, 5, 7]))

# list 인덱스가 실수형이 되었기 때문에 오류가 났었다.(지금은 수정)