## NumPy 인덱싱과 슬라이싱

import numpy as np

scores = np.array([85, 92, 78, 96, 88, 73, 95])

# - 인덱싱: 특정 위치에서 하나 꺼내기 -
print(f"첫번째: {scores[0]}")
print(f"마지막: {scores[-1]}")

# - 슬라이싱: 범위로 여러개 꺼내기 -
print(f"2 ~ 4번째: {scores[1:4]}")

# - 조건 필터링: 조건에 맞는 것만 뽑기 -
print(f"90점 이상: {scores[scores >= 90]}")
print(f"80점 미만: {scores[scores < 80]}")
print(f"평균 이상: {scores[scores >= scores.mean()]}")