# 실습 과제
# 가상의 게임 캐릭터의 현재 상태 값을 입력받고 그 값을 출력
# 이름(문자열), 체력(정수), 보유 골드(정수), 현재 미션 달성도(실수)

name = input("Name : ")
health = int(input("Health : "))
gold = int(input("Gold : "))
mission = float(input("Mission Percent :"))

print(f"Game Character Name is {name}, Health is {health} and Gold id {gold}, Mission is {mission}%")