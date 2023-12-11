# 사용자 입력(user input)
# 변수명 = input("프롬프트") 형태로 input() 함수 이용
# 프롬프트는 입력 받기 전 화면에 표시되는 내용
# 기본적으로 입력 받은 값은 모두 문자열로 취급하며 
# 산술연산을 위해서는 int(), float() 함수를 이용하여 형변환을 해줘야 함.


age = input("Input age : ")
name = input("Yout name : ")

print(f"Your name is {name}, and you are {age} years old.")
print()

x = input("Input x : ")
y = input("Input y : ")

print("x + y = ", x + y)
print()
print("x + y = ", int(x) + int(y))
print("x + y = ", int(x + y))
print()
print("x + y = ", float(x) + float(y))
print("x + y = ", float(x + y))
