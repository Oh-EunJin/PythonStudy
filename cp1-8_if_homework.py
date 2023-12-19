# 실습 과제

# 1. 키(height, m), 몸무게(weight, kg)를 입력 받아 BMI를 계산한 다음 등급 출력
# BMI공식 = 몸무게 / (신장 * 신장)
height = float(input("height : "))
weight = float(input("weight : "))

BMI = weight / (height * height)
if BMI >= 40:
    print("당신은 심각한 비만입니다.")
elif 30 <= BMI < 40:
    print("당신은 비만 2단계입니다.")
elif BMI >= 25 and BMI < 30:
    print("당신은 비만 1단계입니다.")
elif BMI >= 23:
    print("당신은 과체중입니다.")
elif BMI >= 18.5:
    print("당신은 정상입니다.")
else:
    print("당신은 저체중입니다.")
    
print()

# 2. 값1, 연산자(+,-,*,/,%), 값2를 한꺼번에 입력 받아 연산자의 종류에 따라 산술 연산한 결과 출력
x, op, y = input("연산하고자 하는 값 2개와 연산자를 입력해주세요[ex. 3 + 2] : ").split()

if op == "+":
    print(float(x) + float(y))
elif op == "-":
    print(float(x) - float(y))
elif op == "*":
    print(float(x) * float(y))
elif op == "/":
    print(float(x) / float(y))
elif op == "%":
    print(float(x) % float(y))
else:
    print("연산자가 잘못입력되었으니 다시 실행해주세요.")