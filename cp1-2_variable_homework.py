# 실습 과제
# 가상의 게임 캐릭터의 현재 상태 값을 저장하는 변수를 만들고 그 값을 출력
# 이름, 체력(정수), 보유 골드(정수), 현재 등급(S,A,B,C 등 한 글자), 현재 미션 달성도(실수) 등등....

# 변수 선언
name = "짱구"
health = 100
gold = 40000
grade = 'A'
mission = 10.4

# 출력
print("Game Character Name is " , name)
print("health is ", health)
print(f"Gold is {gold}")
# end=''는 파이썬의 print의 줄바꿈 제거하는 역할을 함
print("Grade is ", end='')
print(grade)
print(f"mission is {mission}%")