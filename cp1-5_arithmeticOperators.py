# 산술 연산자(Arithmetic Operators)
x = 10
y = 5

print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x % y = {x % y}")

print()

# 대입 연산자
x += y
print(f"x = {x}")

x -= y
print(f"x = {x}")

x *= y
print(f"x = {x}")

x /= y
print(f"x = {x}")

x %= y
print(f"x = {x}")

print()

# 파이썬만의 연산자
a = 10
b = 3

print(f"a / b = {a / b}")           # 실제 나는 실수값 출력 (3.3333333)
print(f"a // b = {a // b}")         # 정수 부문의 몫 출력 (3)
print(f"a ** b = {a ** b}")         # a ^ b 출력 (1000)

print()

a //= b
print("a = ", a)

a **= b
print("a = ", a)