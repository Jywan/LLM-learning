## Pandas GroupBy - 그룹별 집계
# 설명: Pandas의 GroupBy 기능을 사용하여 데이터를 그룹별로 집계하는 방법을 소개합니다.

import pandas as pd

df = pd.DataFrame({
    "이름": ["영완", "지수", "민준", "수연", "태양"],
    "나이": [32, 28, 35, 24, 30],
    "점수": [85, 92, 78, 96, 88],
    "도시": ["서울", "부산", "서울", "대구", "서울"]
})

# 도시별 평균 점수
print("-- 도시별 평균 점수 --")
print(df.groupby("도시")["점수"].mean())

# 도시별 인원 수
print("\n-- 도시별 인원 수 --")
print(df.groupby("도시")["이름"].count())

# 도시별 여러 통계 한번에 출력
print("\n-- 도시별 점수 통계 --")
print(df.groupby("도시")["점수"].agg(["mean", "max", "min"]))

# 새 열 추가 - 점수 등급
df["등급"] = df["점수"].apply(lambda x: "A" if x >= 90 else "B" if x >= 80 else "C")
print("\n-- 등급 추가 --")
print(df)