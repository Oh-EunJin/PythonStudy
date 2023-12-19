# 조건문(IF문)
# 비교연산 (==, !=, >=, <=)
# 논리연산 (and, or, not)

x = int(input("Input x : "))

if x % 2 == 0:
    print("x is an even number")
else:
    print("x is an odd number")
    
print()
    
score = float(input("Input score(%) : "))
if score >= 90:
    print("Grade Point is A+")
elif score >= 70 and score < 90:
    print("Grade Point is A")
elif 50 <= score < 70:
    print("Grade Point is B")
elif score >= 30:
    print("Grade Point is C")
elif score >= 10:
    print("Grade Point is D")
else:
    print("Grade Point is F")