## NumPy란?
# NumPy는 Numerical Python의 약자로, 파이썬에서 과학적 계산을 위한 핵심 라이브러리입니다.
# 간단하게 풀어 말하자면 파이썬 리스트보다 훨씬 빠르게 숫자도구를 해주는 도구!

import numpy as np

# 테스트 NumPy 배열
scores = np.array([85, 92, 78, 96, 88, 73, 95])

print(f"배열: {scores}")
print(f"SHAPE: {scores.shape}")
print(f"dtype: {scores.dtype}")

# 한번에 계산
print(f"평균: {scores.mean():.1f}")
print(f"최댓값: {scores.max()}")
print(f"최솟값: {scores.min()}")
print(f"합계: {scores.sum()}")

# 리스트와 비교 - NumPy는 한번에!
print(f"10점 추가: {scores + 10}")
print(f"2배: {scores * 2}")