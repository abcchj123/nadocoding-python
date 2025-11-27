'''
# 6.1 조건문에 따라 분기하기 : 조건문
## 6.1.1 조건이 하나일 때 : if 문
weather = "비"

if weather == "비":
    print("우산을 챙기세요")
    
## 6.1.2 조건이 여러 개일 때 : elif 문
weather = "맑음"

if weather == "비":
    print("우산을 챙기세요")
    
weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")  
    
## 6.1.3 모든 조건이 맞지 않을때 : else 문
weather = "맑음"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요.")  
    
## 6.1.4 input()으로 값 입력받아 비교하기
weather = input("오늘 날씨는 어때요? ")
print(weather)

weather = input("오늘 날씨는 어때요? ")
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요.")      

    
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":  
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")                  
else:
    print("준비물이 필요 없어요.")      


temp = int(input("오늘 기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp and temp < 30:
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.") 
     


temp = int(input("오늘 기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요. 외출을 자제하세요.")
elif 10 <= temp < 30:
    print("활동하기 좋은 날씨예요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.") 
 
 
temp = int(input("오늘 기온은 어때요? "))
 
if temp >30:
    print("너무 더워요. 외출을 자제하세요.")
elif temp >=10:
    print("활동하기 좋은 날씨예요.")
elif temp >=0:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.") 


## 6.2 같은 일 반복하기 : 반복문
### 6.2.1 범위 안에서 반복하기 : for 문
for waiting_no in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting_no))
    
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))    

for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))      
    
for waiting_no in range(1,6,2):
    print("대기번호 : {0}".format(waiting_no))          

orders = ["아이언맨","토르","스파이더맨"]
for customer in orders:
    print("{0} 님, 커피가 준비되었습니다. 픽업대로 와 주세요.".format(customer))
    
## 6.2.2 조건을 만족할 동안 반복하기: while 문    
customer = "토르"
index = 5

while index >= 1:
    print("{0} 님, 커피가 준비됐습니다.".format)
    index -= 1
    print("{} 번 남았어요.".format(index))
    if index == 0:
        print("커피는 폐기처분되었습니다.")
        
customer = "아이언맨"
index = 1
while True:
    print("{0} 님, 커피가 준비됐습니다. 호출 {1} 회".format(customer, index))
    index += 1

customer = "토르"
person = "None"
while person != customer:
    print("{0} 님, 커피가 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
   
## 6.2.3 흐름 제어하기: continue와 break
absent = [2,5]  # 결석
for student in range(1,11):  # 1~10 학생
    if student in absent:
        continue
    print("{0} 번 학생, 책을 읽어 보세요.".format(student))

absent = [2,5]  # 결석
no_book = [7]  # 책 없음
for student in range(1,11):  # 1~10 학생
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0} 번 학생은 교무실로 따라와요.".format(student))
        break
    print("{0} 번 학생, 책을 읽어 보세요.".format(student))

## 6.2.4 for 문 한 줄로 작성하기
students = [1,2,3,4,5]
print(students)

students = [i + 100 for i in students]
print(students)

students = ["Iron mon", "Thor", "Spider man"]
print(students)

students = [len(i) for i in students]
print(students)

## 6.3 실습 문제 : 택시 승객 수 구하기
"""
당신은 Cocoa 서비스를 이용하는 택시기사입니다. 
손님이 총 50명일 때, 조건을 만족하는 총 탑승객 수를 구하는 프로그램을 작성하세요.

조건
1. 손님별 운행 소요시간은 5~50분에서 난수
2. 운행 소요시간 5~15분인 손님만 매칭
3. 실행 결과는 다음 형태로 출력, 매칭되면 [0], 매칭되지 않으면 []로 표시
"""

from random import *
cnt = 0  # 탑승 승객 수
for i in range(1,51):  # 1~50 손님
    time = randrange(5,51)  # 5~50분 소요 시간
    if 5 <= time <= 15:  # 매칭 성공 조건
        print("[O] {0} 번째 손님 (소요시간 : {1} 분)".format(i, time))
        cnt += 1
    else:  # 매칭 실패 조건
        print("[ ] {0} 번째 손님 (소요시간 : {1} 분)".format(i, time))
print("총 탑승 승객 : {0} 분".format(cnt))
'''
## 셀프체크
"""
편의점에서 동일한 상품을 2개를 구매하면 상품 1개를 무료로 제공하는 2+1 이벤트를 진행하고 있습니다.
구매 상품 수에 따라 가격을 계산하는 프로그램을 작성하세요.

조건
1. 상품 가격은 1개당 1,000원
2. 고객은 3,6,9.... 처럼 항상 3의 배수에 해당하는 상품을 구매
3. 상품을 각각 스캔하며, 한 상품을 스캔할 때마다 '2+1 상품입니다.'를 출력한다.

----실행 결과----
2+1 상품입니다.
2+1 상품입니다.
2+1 상품입니다.
총 가격은 2000원입니다

"""
product_price = 1000  # 상품 가격
num = int(input("구매할 상품 수를 입력하세요: "))  # 구매 상품 수
total_price = 0  # 총 가격
for i in range(1, num + 1):
    print("2+1 상품입니다.")    
    if i % 3 != 0:
        total_price += product_price
        
print("총 가격은 {0}원입니다.".format(total_price))