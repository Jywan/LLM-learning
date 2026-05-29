## Pandas
# Pandas란 데이터 분석을 위한 라이브러리
# 데이터 조작과 분석에 필요한 다양한 기능을 제공
# Numpy는 숫자만 다루지만 Pandas는 숫자, 문자열, 날짜 등 다양한 데이터 타입을 다룰 수 있음

import pandas as pd

# DataFrame 만들기
df = pd.DataFrame({
    "이름": ["영완", "지수", "민준", "수영", "태양"],
    "나이": [32, 28, 35, 24, 30],
    "점수": [85, 92, 78, 96, 88],
    "도시": ["서울", "부산", "서울", "대구", "서울"]
})

# 기본정보 확인
print(df)               # 표 전체 출력
print()
print(df.shape)         # (행 수, 열 수)
print(df.dtypes)        # 각 열의 자료형
print()
print(df.describe())    # 숫자 열 통계 요약 (평균, 최대, 최소 등)