## NumPy 2차원 배열
# 행(row) x 열(column) 형태의 2차원 배열

import numpy as np

# 3명 학생의 국, 영, 수 점수
scores = np.array([[85, 92, 78], [96, 88, 73], [95, 70, 88]])

print(f"shape: {scores.shape}") # 행×열

print(f"1번 학생 전체: {scores[0]}")
print(f"1번 학생 영어: {scores[0][1]}")

print(f"전체 국어 점수: {scores[:, 0]}") # 모든 행에서 0번째 열
print(f"전체 영어 점수: {scores[:, 1]}") # 모든 행에서 1번째 열

print(f"과목별 평균: {scores.mean(axis=0)}") # 열 방향 평균(과목별)
print(f"학생별 평균: {scores.mean(axis=1)}") # 행 방향 평균(학생별)
