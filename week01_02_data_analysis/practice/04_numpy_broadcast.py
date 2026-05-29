## 브로드캐스팅
# 크키가 다른 배열끼리 연살할깨 NumPy가 자동으로 맞춰서 계산해주는 기능

import numpy as np

scores = np.array([[85, 92, 78], [96, 88, 73], [95, 70, 88]])

# 전체 +5 보정
print("전체 +5:")
print(scores + 5)

# 과목별 보정
bouns = np.array([5, 3, 2])
print("\n과목별 보정 후 :")
print(scores + bouns)

# 평균으로 정규화 (0 중심으로 맞추기)
mean = scores.mean(axis=0)
print(f"\n과목별 평균:")
print(mean)
print("\n평균 제거 후:")
print(scores - mean)
