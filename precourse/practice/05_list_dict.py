# 리스트
scores = [85, 92, 78, 96, 88]

print("전체 점수:", scores)
print("첫 번째 점수:", scores[0])
print("마지막 점수:", scores[-1])
print("평균", sum(scores) / len(scores))

scores.append(100)
scores.sort()
print("정렬 후: ", scores)

print("-----------")

# 딕셔너리

me = {
    "name": "영완",
    "age": 32,
    "height": 181,
    "hobbies": ["코딩", "운동", "독서"] 
}

print("이릅: ", me["name"])
print("취미: ", me["hobbies"])

# 딕셔너리에 새 항목 추가
me["job"] = "개발자"
print("직업: ", me["job"])