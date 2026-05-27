# 형 변환
num_str = "100"
num_int = int(num_str)
print(f"문자열 -> 정수: {num_int + 50}")

pi = 3.14159
print(f"실수 -> 정수: {int(pi)}")


# f string
name = "영완"
age = 32
height = 181
bmi = 70 / (height / 100) ** 2

print(f"이름: {name}")
print(f"나이: {age}")
print(f"BMI: {bmi:.2f}")