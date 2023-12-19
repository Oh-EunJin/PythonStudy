# 실습 과제

# 1. 두 정수 x,y를 입력 받아 사칙 연산과 나머지 연산한 결과 출력
x = int(input("x : "))
y = int(input("y : "))

print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x /% y = {x % y}")

print()

# 2. 키(height, m), 몸무게(weight, kg)를 입력 받아 BMI 지수를 구해 출력
# BMI공식 = 몸무게 / (신장 * 신장)
height = float(input("height : "))
weight = float(input("weight : "))

print(f"BMI = {weight / (weight * weight)}")