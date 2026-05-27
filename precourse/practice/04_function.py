# 나이에 따라 다른 메시지를 출력하는 함수
def check_age(age):
    if age >= 30:
        return "30대 입니다."
    elif age >= 20:
        return "20대 입니다."
    else:
        return "10대 이하입니다."
    
# 키를 받아서 BMI 구하는 함수
def get_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

# response
print(check_age(32))
print(check_age(25))

bmi = get_bmi(70, 181)
print("BMI:", bmi)