# 변수 퀴즈

# 1. break

# 2. 1break

# 3. break* 

# 4. break1

# 5. break 1 

# # *** 서식 문자 출력 ***

# #예제1. 자신의 이름, 나이, 사는곳을 변수에 담아 출력
# name = "펭수"
# age = 20
# address = "남극"

# print("{} 님의 나이는 {} 세 이며, 사는곳은 {} 입니다.".format(name,age,address))
# print(name,"님의 나이는",age,"세 이며, 사는곳은",address,"입니다.")

# #예제2. 자신의 키, 몸무게를 변수에 담아 출력
# height = 180
# weight = 90

# print("펭수님의 키는 {}cm 이며, 몸무게는 {}kg 입니다.".format(height,weight))

# #예제3. ? + ? = 30과 같은 결과가 나오도록 변수 설정 및 출력
# su1 = 10
# su2 = 20

# print("{} + {} = {}".format(su1,su2,su1+su2))

# #예제4. 이름과 출생년도를 변수에 담아 만나이 출력
# name = "펭수"
# b_year = 2002

# print("{}님의 만나이는 {}세 입니다.".format(name,2022-b_year))

# #예제5. 실수를 변수에 담아 실수의 제곱 출력
# f = 3.0
# print("{:f}".format(f*f))
# print("{:.1f}".format(f*f))

# print("{:f}".format(f**2))
# print("{:.1f}".format(f**3))

# #예제6. 정수3개 변수에 담아 그 합과 평균을 출력
# a = 10
# b = 20
# c = 30

# print("합: {}\t평균: {}".format(a+b+c,(a+b+c)/3))

# #예제7. 자유롭게 변수에 담아 출력(다한 사람만)
# a = 10
# b = 20
# c = 30

# sum1 = a + b + c

# print("합: {}\t평균: {}".format(sum1,sum1/3))



# # 변수 : 변할 수 있는 값

# # 예시
# a = "안녕하세요"

# a = "반갑습니다"

# print(a)

# # 입력 input

# a = input("성함: ")

# print(a)

# # 문제1

# name = input("성함: ")

# age = input("나이: ")

# email = input("이메일: ")

# print("{}님의 나이는 {}세이며, 이메일은 {} 입니다.".format(name,age,email))


# # 문제2
# a = int(input("수입력: "))
# b = int(input("수입력: "))

# print(a+b)
# print(a-b)


# #1번
# print(type(a))
# print(type(b))

# #2번
# a = int(a)
# b = int(b)

# print(a+b)
# print(a-b)

# # 3번
# c = input("수입력: ")
# d = input("수입력: ")
# e = input("수입력: ")

# print(int(a)+int(b)+int(c)+int(d)+int(e))
# print(int(a)-int(b)-int(c)-int(d)-int(e))

# # 문제3

# m = int(input("수학: "))
# e = int(input("영어: "))
# p = int(input("파이썬: "))

# print("평균 :{}점".format((m+e+p)/3))
# print("평균 :{}점".format((m+e+p)/3))
# print("평균 :{}점".format((m+e+p)/3))

# #비교
# m = int(input("수학: "))
# e = int(input("영어: "))
# p = int(input("파이썬: "))

# avr = (m+e+p)/3

# print("평균 :{}점".format(avr))
# print("평균 :{}점".format(avr))
# print("평균 :{}점".format(avr))


# # 문제4
# apple_p = 4000
# pear_p = 3000

# print("*** 사과 {:,}원 배 {:,}원 ***".format(apple_p,pear_p))

# apple = int(input("사과 개수: "))
# pear = int(input("배 개수: "))

# total = apple * apple_p + pear * pear_p

# print("총금액 : {:,}원" .format(total))

# #문제5

# t = int(input("시간: "))
# m = int(input("분: "))
# s = int(input("초: "))

# total_s = t*3600 + m*60 + s

# print("총초 > {}초".format(total_s))
