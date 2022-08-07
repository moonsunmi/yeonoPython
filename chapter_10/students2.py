import stats

# 기말고사 성적
scores = [99, 98, 96, 100, 99, 92, 93, 27, 96, 85, 100, 99]
# 학생들의 키
heights = [155.8, 182.7, 166.3, 181.1, 179.5, 173.2, 174.5, 162.3]
# 칭찬 도장을 받은 학생
compliments = ['박연오', '김파이', '김파이', '박연오', '박연오']

print('기말고사 성적 평균:', stats.mean(scores))
print('가운데 앉은 학생의 키:', stats.median(heights))
print('칭찬을 가장 많이 받은 학생:', stats.most_frequent(compliments))
