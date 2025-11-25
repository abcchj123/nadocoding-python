## 5.1.1 리스트 생성하기
# 지하철 칸마다 사람들이 몇 명씩 타고 있는지 다음과 같이 변수로 나타냄
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)
## 5.1.2 값 추가/삽입/삭제하기
subway = ["푸","피그렛","티거"]
print(subway)

# 피그렛이 몇 번째 칸에 탔는가?
print(subway.index("피그렛"))

# 이요르 탑승
subway.append("이요르")
print(subway)   

subway.insert(1, "루")
print(subway)

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.clear()
print(subway)

## 5.1.3 중복 값 확인하기
subway = ["푸","피그렛","티거"]
subway.append("푸")
print(subway)
print(subway.count("푸"))

## 5.1.4 리스트 정렬하기
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)

num_list.reverse()
print(num_list)

## 5.1.5 리스트 확장하기
mix_list = ["푸",20,True,[5,4,3,2,1]]
print(mix_list)

mix_list = ["푸",20,True]
num_list = [5,4,3,2,1]
mix_list.extend(num_list)
print(mix_list)
print(num_list)

# 5.2 딕셔너리
## 5.2.1 딕셔너리 생성하기
cabinet = {3:"푸", 100:"피그렛"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet.get(5))
print("하이")
print(cabinet[5])
print("하이")

print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

print("곰" in "곰돌이")
print("돌이" in "곰돌이")
print("푸" in "곰돌이")

## 5.2.2. 값 변경/추가/삭제하기
cabinet = {"A-3":"푸", "B-100":"피그렛"}
print(cabinet) 
cabinet["A-3"] = "티거"
cabinet["C-20"] = "이요르"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

## 5.2.3. 값 확인하기
print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

#5.3 튜플
menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])  

name = "피그렛"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("피그렛", 20, "코딩")
print(name, age, hobby)

(departure, arrival) = ("김포", "제주")
print(departure, ">", arrival)
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival)

# 5.4 세트
my_set = {1,2,3,3,3}
print(my_set)

java = {"푸","피그렛","티거"}
python = set(["푸","이요르"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("피그렛")
print(python)

# 5.5 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

## 5.6 실습문제
"""
파이썬 코딩 대회가 열림. 참석률을 높히기 위해 댓글 이벤트를 진행.
작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받음.
추첨 프로그램 작성하기

1. 편의상 댓글은 20명이 작성했다고 가정, 아이디는 1~20
2. 무작위 추첨하되 중복은 허용하지 않는다. 
3. random 모듈의 shuffle과 sample을 활용
4. 실행결과는 다음과 같이 표하시하고 치킨 당첨자 1명, 커피 당첨자 3명 출력
-- 당첨자 발표 --
치킨 당첨자 : 6
커피 당첨자 : [9, 3, 10]
-- 축하합니다 --
"""
    
import random
users = range(1, 21) # 1~20까지 숫자 생성
users = list(users)
random.shuffle(users)
winners = random.sample(users, 4) # 4명 중에서 1명
chicken = winners[0]
coffee = winners[1:]
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken))
print("커피 당첨자 : {0}".format(coffee))
print("-- 축하합니다 --")

## 셀프체크
"""
나도대학교에서 수강신청 기간에 시스템 오류로 일부 과목이 중복 신청되는 사태가 발생.
중복 신청된 과목을 없애는 프로그램 작성하기

조건 
1. 신청 과목은 리스트로 제공
2. 리스트에 같은 과목이 2번 이상 포함된 경우 1개만 남기고 나머지 삭제
3. 출력 시 신청 과목의 순서는 상관없음

"""

subjects = ["파이썬", "자바", "파이썬", "C언어", "파이썬", "자바스크립트", "자바"]
subjects = set(subjects)
subjects = list(subjects)
print("신청한 과목은 다음과 같습니다.")
print(subjects) 