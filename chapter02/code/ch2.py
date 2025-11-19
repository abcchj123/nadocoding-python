# 2.1 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)


print(5+3)
print(2*8)
print(6/3)
print(3*(3+1))

# 2.2 문자열 자료형
print('풍선')
print("나비")
print("abcdfg")
print("10")
print("파이썬" *3)

#오류 발생 구분
#print('작은따옴표")
#print("큰따옴표')

# 2.3 불자료형
print(5>10)
print(5<10)

print(True)
print(False)

print(not True)
print(not False)

print(not (5>10))

# 2.4
# 2.4.1 변수 정의하기
print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요.")
print("연탄이는 4살이고, 산책을 아주 좋아해요.")
print("연탄이는 수컷인가요?")
print("네.")

name = "연탄이"
animal = "개"
age = 4
hobby = "산책"
is_male = True

# 2.4.2 변수 사용하기
print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.")
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")

name = "해피"
animal = "고양이"
age = 4
hobby = "낮잠"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.")
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")

name = "연탄이"
animal = "개"
age = 4
hobby = "산책"
is_male = True

print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.")
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")
print(name,"는 ",age,"살이고, ",hobby,"을 아주 좋아해요.")

#2.4.3 형변환하기

print(int("3"))
#print(int("3") + "입니다.") < - 정수형 + 문자열로 형 불일치
print(int(3.5))  #r결과 : 3
#print(int("삼")) #오류발생

print(float("3.5"))
print(float(3)) # 결과 : 3.0
#print(float("오")) #오류발생

print(str("3")+"입니다.")
print(str("3.5")+"입니다.")

print(type(3))      #결과 : <class 'int'>
print(type("3"))    #결과 : <class 'str'>
print(type(3.5))    #결과 : <class 'float'>
print(type(str("3"))) #결과 : <class 'str'>

#2.4.4 변수를 사용할 때 유의할 점
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
#print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.") #오류 발생
name = "연탄이"
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")

name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.")
hobby = "수영"
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")


#2.5 주석
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

#print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.")
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")


name = "연탄이"
animal = "개"
age = 4
hobby = "산책"

""""
#print("반려동물을 소개해 주세요.")
print("우리 집 반려동물은 " + animal + "인데, 이름이 "+name+ "이예요.")
print(name+"는 "+str(age)+"살이고, "+hobby+"을 아주 좋아해요.")
"""

#2.6 실습문제 
## 변수를 이용하여 문장을 출력
### 변수명은 station 
### 변수에 "사당, 신도림, 인천공항"순으로 저장한다.
### 결과는 변수에 "사당"을 넣었을때 -> "사당행 열차가 들어오고 있습니다."

station = "사당"
#station = "신도림"
#station = "인천"
print(station+"행 열차가 들어오고 있습니다.")

# 셀프 체크 
## 변수를 이용하여 택배의 배송 상태를 안내하는 프로그램을 작성
### 변수명은 status
### 변수에 "상품 준비, 배송 중, 배송 완료"순으로 저장한다.
### 결과는 변수에 "상품 준비"을 넣었을때 -> "주문상태 : 상품 준비"
statue = "상품 준비"
#statue = "배송 중"
#statue = "배송 완료"
print("주문상태 : "+ statue)