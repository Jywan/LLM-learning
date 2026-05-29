# Pandas NaN
# NaN(Not a Number)은 숫자가 아닌 값을 나타내는 특별한 값입니다. 
# Pandas에서는 NaN을 사용하여 결측값(missing value)을 나타냅니다. 
# NaN은 주로 데이터 분석에서 누락된 데이터를 처리할 때 사용됩니다.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "이름": ["영완", "지수", "민준", "수연", "태양"],
    "나이": [32, np.nan, 35, 24, 30],
    "점수": [85, 92, np.nan, 96, 88],
    "도시": ["서울", "부산", None, "대구", "서울"]
})

print("-- 원본 데이터--")
print(df)

print("\n-- NaN 위치 확인 --")
print(df.isnull().sum())    # 열별 NaN 개수 확인

print("\n-- 평균으로 채우기 --")
df["점수"] = df["점수"].fillna(df["점수"].mean())    # 점수 열의 NaN을 평균으로 채우기
print(df["점수"])

print("\n-- NaN 행 삭제 --")
df_clean = df.dropna()    # NaN이 있는 행 삭제
print(df_clean)