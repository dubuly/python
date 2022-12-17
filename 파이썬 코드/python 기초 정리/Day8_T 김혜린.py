# #문제1
# m = int(input("수학 점수: "))
# s = int(input("과학 점수: "))

# avr = ( m + s ) / 2

# if avr >= 90:
#     print("평균: {} 점. 이번학기 성적은 A 입니다.".format(avr))

# elif avr >= 80:
#     print("평균: {} 점. 이번학기 성적은 B 입니다.".format(avr))

# elif avr >= 70:
#     print("평균: {} 점. 이번학기 성적은 C 입니다.".format(avr))

# else:
#     print("평균: {} 점. 이번학기 성적은 D 입니다.".format(avr))

# #문제2
# su1 = int(input("수입력: "))
# su2 = int(input("수입력: "))
# e = input("연산자 입력: ")

# if e == "+":
#     print("{} + {} = {}".format(su1,su2,su1+su2))
# elif e == "-":
#     print("{} - {} = {}".format(su1,su2,su1-su2))
# elif e == "*":
#     print("{} * {} = {}".format(su1,su2,su1*su2))
# elif e == "/":
#     print("{} / {} = {}".format(su1,su2,su1/su2))
# else:
#     print("연산자가 이상해요.")

#문제3

# m = int(input("월을 입력하세요: "))

# if 1 <= m <= 3:
#     print("{}월은 봄 입니다.".format(m))

# elif 4 <= m <= 6:
#     print("{}월은 여름 입니다.".format(m))

# elif 7 <= m <= 9:
#     print("{}월은 가을 입니다.".format(m))

# elif 10 <= m <= 12:
#     print("{}월은 겨울 입니다.".format(m))

# else:
#     print("잘못입력하셨습니다.")


# # 추가
# m = int(input("월을 입력하세요: "))

# if 1 <= m <= 12:
#     if m <= 3:
#         print("{}월은 봄 입니다.".format(m))

#     elif m <= 6:
#         print("{}월은 여름 입니다.".format(m))

#     elif m <= 9:
#         print("{}월은 가을 입니다.".format(m))

#     elif m <= 12:
#         print("{}월은 겨울 입니다.".format(m))
# else:
#     print("잘못입력하셨습니다.")

# # 문제4
# n = int(input("수입력: "))

# if n >= 0:
#     print("절대값은 {} 입니다.".format(n))

# else:
#     print("절대값은 {} 입니다.".format(-n))

# # 함수
# print("절대값은 {} 입니다.".format(abs(n)))

# #문제5
# apple = int(input("사과: "))
# pear = int(input("배: "))
# m = int(input("소지한 금액: "))

# total_p = apple * 3000 + pear * 2000

# # 1. 현금 - 총금액 0보다 큰 경우 아닌경우
# if m - total_p >= 0:
#     print("구매가능. 잔액: {:,}원".format(m-total_p))

# else:
#     print("구매 불가. 필요한 금액: {:,}원".format(-(m-total_p)))


# # 2. 현금이 총금액보다 큰 경우 아닌경우
# if m >= total_p:
#     print("구매가능. 잔액: {:,}원".format(m-total_p))

# else:
#     print("구매 불가. 필요한 금액: {:,}원".format(-(m-total_p)))


# # 문제6
# a = int(input("수입력: "))

# if a % 15 == 0:
#     print("{}은 15의 배수".format(a))

# elif a % 3 == 0:
#     print("{}은 3의 배수".format(a))

# elif a % 5 == 0:
#     print("{}은 5의 배수".format(a))

# else:
#     print("해당 조건X")


# #문제7
# 이름 = input("성함: ")
# 키 = float(input("키: "))
# 체중 = float(input("체중: "))

# 표준체중 = (키 -100)*0.9
# 비만도 = 체중/표준체중*100

# print("{}님의 비만도는 {:.2f} 입니다.".format(이름,비만도))

# if 비만도 < 100:
#     print("저체중")

# elif 100 <= 비만도 < 110:
#     print("정상")

# elif 110 <= 비만도 < 120:
#     print("과체중")

# elif 120 <= 비만도 < 130:
#     print("비만")

# else:
#     print("고도비만")

# # 문제8 
# n = int(input("몇일? "))

# if n % 4 == 1:
#     print("{}일. A가 당번 입니다.".format(n))

# elif n % 4 == 2:
#     print("{}일. B가 당번 입니다.".format(n))

# elif n % 4 == 3:
#     print("{}일. C가 당번 입니다.".format(n))

# else:
#     print("{}일. D가 당번 입니다.".format(n))


# #문제9 
# n = int(input("N일 후는 몇요일?"))

# if n % 7 == 1:
#     print("{}일 후는 수요일 입니다.".format(n))

# elif n % 7 == 2:
#     print("{}일 후는 목요일 입니다.".format(n))

# elif n % 7 == 3:
#     print("{}일 후는 금요일 입니다.".format(n))

# elif n % 7 == 4:
#     print("{}일 후는 토요일 입니다.".format(n))

# elif n % 7 == 5:
#     print("{}일 후는 일요일 입니다.".format(n))

# elif n % 7 == 6:
#     print("{}일 후는 월요일 입니다.".format(n))

# else:
#     print("{}일 후는 화요일 입니다.".format(n))


# # 문제10 

# a = int(input("수입력: "))
# b = int(input("수입력: "))

# # 123

# r_a = a % 10 * 100 + a // 10 % 10 * 10 + a // 100
# r_b = b % 10 * 100 + b // 10 % 10 * 10 + b // 100

# # print(r_a)
# # print(r_b)

# if r_a > r_b:
#     print("큰 수 : {}".format(a))

# elif r_a < r_b:
#     print("큰 수 : {}".format(b))

# else:
#     print("두 수는 같습니다.")


# #문제12
# year = int(input("태어난 년도를 입력하세요: "))

# y = year % 12

# #2022

# if y == 0:
#     print("{}년 -> 원숭이 띠".format(year))

# elif y == 1:
#     print("{}년 -> 닭 띠".format(year))

# elif y == 2:
#     print("{}년 -> 개 띠".format(year))

# elif y == 3:
#     print("{}년 -> 돼지 띠".format(year))

# elif y == 4:
#     print("{}년 -> 쥐 띠".format(year))

# elif y == 5:
#     print("{}년 -> 소 띠".format(year))

# elif y == 6:
#     print("{}년 -> 범 띠".format(year))

# elif y == 7:
#     print("{}년 -> 토끼 띠".format(year))

# elif y == 8:
#     print("{}년 -> 용 띠".format(year))

# elif y == 9:
#     print("{}년 -> 뱀 띠".format(year))

# elif y == 10:
#     print("{}년 -> 말 띠".format(year))

# elif y == 11:
#     print("{}년 -> 양 띠".format(year))


# # 문제12

# # 1번 - 쉬운 방법
# year = int(input("년도: "))

# if year % 400 == 0:
#     print("{}년 > 윤년".format(year))

# elif year % 100 == 0:
#     print("{}년 > 평년".format(year))

# elif year % 4 == 0:
#     print("{}년 > 윤년".format(year))

# else:
#     print("{}년 > 평년".format(year))

# # 2번 - 간단한 방법
# year = int(input("년도: "))

# if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
#     print("{}년 > 윤년".format(year))
# else:
#     print("{}년 > 평년".format(year))

# # 3번 - 중첩 if문 사용(어려운 방법)

# # 1200 , 1100 , 244 , 243 순서대로 대입....!

# year = int(input("년도: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("{}년 > 윤년".format(year))
#         else:
#             print("{}년 > 평년".format(year))
#     else:
#         print("{}년 > 윤년".format(year))
# else:
#     print("{}년 > 평년".format(year))


# # 생각해보기

# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# num3 = int(input("수입력: "))

# if num1 > num2:
#     if num1 > num3:
#         print("가장 큰 수 : {}".format(num1))

# elif num2 > num1:
#     if num2 > num3:
#         print("가장 큰 수 : {}".format(num2))

# else:
#     print("가장 큰 수 : {}".format(num3))

# # 1,2,3 순서대로 입력시 3이 출력 안되는 이유는....?


# 조건문 연습 (5단계 - 숙제)

# 문제13번 문제14번은 조건식 사용X

# 문제14번 0시 20분 입력시 11시 50분 나오게 해보기!

# 문제15번 커피 전문점 어플을 참고해서 메뉴 여러개 추가해보기! 
