# 문제 1
# a = int(input("수입력: "))
# if a % 10 % 2 == 0:
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 홀수".format(a))

# print("1. easy game")
# print("2. hard game")
# print("3. exit")
# c = int(input("선택: "))
# if c == 1:
#     print("easy game start")
# elif c == 2:
#     print("hard game start")
# elif c == 3:
#     print("exit")

# m = int(input("수학 성적: "))
# s = int(input("과학 성적: "))
# avr = (m+s)/2

# if avr > 90:
#     print("평균: {} 성적: A".format(avr))
# elif 80 <= avr < 90:
#     print("평균: {} 성적: B".format(avr))
# elif 70 <= avr < 80:
#     print("평균: {} 성적: C".format(avr))
# else:
#     print("평균: {} 성적: D".format(avr))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = input("연산자: ")

# if c == "+":
#     print("{} + {} = {}".format(a,b,a+b))
# elif c == "-":
#     print("{} - {} = {}".format(a,b,a-b))
# elif c == "*":
#     print("{} * {} = {}".format(a,b,a*b))
# elif c == "/":
#     print("{} / {} = {}".format(a,b,a/b))
# else:
#     print("연산자가 이상해요")

# m = int(input("몇월? "))

# if 1 <= m <= 3:
#     print("{}월은 봄입니다.".format(m))
# elif 4 <= m <= 6:
#     print("{}월은 여름입니다.".format(m))
# elif 7 <= m <= 9:
#     print("{}월은 가을입니다.".format(m))
# elif 10 <= m <= 12:
#     print("{}월은 겨울입니다.".format(m))
# else:
#     print("입력이 바르지 않습니다")

# n = int(input("수입력: "))

# if n > 0:
#     print("절대값은 {} 입니다".format(n))
# elif n < 0:
#    print("절대값은 {} 입니다".format(-n))
# else:
#     print("절대값은 0 입니다")

# apple_p = 3000
# pear_p = 2000

# apple = int(input("사과 개수: "))
# pear = int(input("배 개수: "))
# m = int(input("소지 금액: "))
# total = apple_p * apple + pear_p * pear

# if total <= m:
#     print("구매 가능. 잔돈: {:,}원".format(m-total))
# elif total > m:
#     print("구매 불가. 필요한 금액: {:,}원".format((total-m)))

# a = int(input("수입력: "))

# if a % 15 == 0:
#     print("{}는 15의 배수 입니다".format(a))
# elif a % 3 == 0:
#     print("{}는 3의 배수 입니다.".format(a))
# elif a % 5 == 0:
#     print("{}는 5의 배수 입니다.".format(a))
# else:
#     print("잘못 입력하셨습니다")


# name = input("이름: ")
# height = int(input("키: "))
# weight = int(input("체중: "))
# 표준체중 = (height-100)*0.9
# 비만도 = weight/((height-100)*0.9)*100

# if 비만도 < 100:
#     print("비만도: {}, 저체중".format(비만도))
# elif 100 <= 비만도 < 110:
#     print("비만도: {}, 정상".format(비만도))
# elif 110 <= 비만도 < 120:
#     print("비만도: {}, 과체중".format(비만도))
# elif 120 <= 비만도 < 130:
#     print("비만도: {}, 비만".format(비만도))
# else:
#     print("비만도: {}, 고도 비만".format(비만도))



# n = int(input("몇 일? "))
# if n % 4 == 0:
#     print("청소 당번: D, 몇일? {}".format(n))
# elif n % 4 == 1:
#     print("청소 당번: A, 몇일? {}".format(n))
# elif n % 4 == 2:
#     print("청소 당번: B, 몇일? {}".format(n))
# elif n % 4 == 3:
#     print("청소 당번: C, 몇일? {}".format(n))

# n = int(input("N일 후? "))
# if n % 7 == 1:
#     print("{}일후, 수요일".format(n))
# elif n % 7 == 2:
#     print("{}일후, 목요일".format(n))
# elif n % 7 == 3:
#     print("{}일후, 금요일".format(n))
# elif n % 7 == 4:
#     print("{}일후, 토요일".format(n))
# elif n % 7 == 5:
#     print("{}일후, 일요일".format(n))
# elif n % 7 == 6:
#     print("{}일후, 월요일".format(n))
# elif n % 7 == 0:
#     print("{}일후, 화요일".format(n))

# y = int(input("태어난 연도: "))
# if y % 12 == 0:
#     print("태어난 연도: {} 원숭이띠".format(y))
# elif y % 12 == 1:
#     print("태어난 연도: {} 닭띠".format(y))
# elif y % 12 == 2:
#     print("태어난 연도: {} 개띠".format(y))
# elif y % 12 == 3:
#     print("태어난 연도: {} 돼지띠".format(y))
# elif y % 12 == 4:
#     print("태어난 연도: {} 쥐띠".format(y))
# elif y % 12 == 5:
#     print("태어난 연도: {} 소띠".format(y))
# elif y % 12 == 6:
#     print("태어난 연도: {} 범띠".format(y))
# elif y % 12 == 7:
#     print("태어난 연도: {} 토끼띠".format(y))
# elif y % 12 == 8:
#     print("태어난 연도: {} 용띠".format(y))
# elif y % 12 == 9:
#     print("태어난 연도: {} 뱀띠".format(y))
# elif y % 12 == 10:
#     print("태어난 연도: {} 말띠".format(y))
# else:
#     print("태어난 연도: {} 양띠".format(y))

# a = int(input("세자리수: "))
# b = int(input("세자리수: "))
# a_d = a % 10 * 100 + a // 10 % 10 * 10 + a // 100
# b_d = b % 10 * 100 + b // 10 % 10 * 10 + b // 100

# if a_d > b_d:
#     print("큰 수: {}".format(a_d))
# elif a_d < b_d:
#     print("큰 수: {}".format(b_d))
# else:
#     print("두 수는 같다")

