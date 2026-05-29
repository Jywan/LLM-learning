## Matplotlib
# 설명: Matplotlib은 Python에서 가장 널리 사용되는 데이터 시각화 라이브러리입니다. 
# 다양한 유형의 그래프와 차트를 생성할 수 있으며, 데이터 분석과 시각화를 위한 강력한 도구입니다.
# 그래프 종류 : 
# 1. 선 그래프 (Line Plot) : plot() - 시간에 따른 데이터의 변화를 시각화하는 데 사용됩니다.
# 2. 막대 그래프 (Bar Plot) : bar() - 카테고리별 데이터의 크기를 비교하는 데 사용됩니다.
# 3. 히스토그램 (Histogram) : hist() - 데이터의 분포를 시각화하는 데 사용됩니다.
# 4. 산점도 (Scatter Plot) : scatter() - 두 변수 간의 관계를 시각화하는 데 사용됩니다.

import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (MacOS)
plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False

scores = [85, 92, 78, 96, 88, 73, 95]
names = ["영완", "지수", "민준", "수연", "태양", "하늘", "도현"]

# -- 1. 선 그래프 --
plt.figure(figsize=(8, 4))  # 그래프 크기 설정
plt.plot(names, scores, marker="o", color="tomato")
plt.title("학생별 점수 추이")
plt.xlabel("이름")
plt.ylabel("점수")
plt.grid(True)              # 격자 추가
plt.savefig("week01_02_data_analysis/practice/line_chart.png")    # 그래프 저장
plt.show()

# -- 2. 막대 그래프 --
plt.figure(figsize=(8, 4))
plt.bar(names, scores, color="steelblue")    # 막대 그래프 생성
plt.title("학생별 점수")
plt.xlabel("이름")
plt.ylabel("점수")
plt.ylim(60, 100)   # y축 범위 설정
plt.savefig("week01_02_data_analysis/practice/bar_chart.png")    # 그래프 저장
plt.show()

# -- 3. 히스토그램 --
data = np.random.normal(75, 10, 200)    # 평균 75, 표준편차 10, 데이터 개수 200인 정규분포 데이터 생성
plt.figure(figsize=(8, 4))
plt.hist(data, bins=20, color="mediumseagreen", edgecolor="white")    # 히스토그램 생성
plt.title("점수 분포")
plt.xlabel("점수")
plt.ylabel("빈도")
plt.savefig("week01_02_data_analysis/practice/histogram.png")    # 그래프 저장
plt.show()