# 문제 1

# m = int(input("수학 성적: "))
# s = int(input("과학 성적: "))
# avg = (m+s)/2
# if avg >= 90:
#     print("평균: {}점. 이번 학기 성적은 A 입니다.".format(avg))
# elif avg >= 80:
#     print("평균: {}점. 이번 학기 성적은 B 입니다.".format(avg))
# elif avg >= 70:
#     print("평균: {}점. 이번 학기 성적은 C 입니다.".format(avg))
# else:
#    print("평균: {}점. 이번 학기 성적은 D 입니다.".format(avg))

# 문제 2

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# e = input("연산자: ")

# if e == "+":
#     print("{} + {} = {}".format(a,b,a+b))
# elif e == "-":
#     print("{} - {} = {}".format(a,b,a-b))
# elif e == "*":
#     print("{} * {} = {}".format(a,b,a*b))
# elif e == "/":
#     print("{} / {} = {}".format(a,b,a/b))
# else:
#     print("연산자가 이상해요.")

# 문제 3

# m = int(input("월: "))
# if 1 <= m <= 3:
#     print("{}월은 봄입니다.".format(m))
# elif 4 <= m <= 6:
#     print("{}월은 여름입니다.".format(m))
# elif 7 <= m <= 9:
#     print("{}월은 가을입니다.".format(m))
# elif 10 <= m <= 12:
#     print("{}월은 겨울입니다.".format(m))
# else:
#     print("입력이 바르지 않습니다!")

# 정방향으로 흘러갈 경우 앞에 범위를 지정 하지 않아도 된다
# 중첩 if문 활용
# m = int(input("월: "))
# if 1 <= m <= 12:
#     if m <= 3:
#         print("{}월은 봄입니다.".format(m))
#     elif m <= 6:
#         print("{}월은 여름입니다.".format(m))
#     elif m <= 9:
#         print("{}월은 가을입니다.".format(m))
#     elif m <= 12:
#         print("{}월은 겨울입니다.".format(m))
# else:
#     print("입력이 바르지 않습니다!")

# 문제 4
# a = int(input("수입력: "))
# if a >= 0:
#     print("절대값은 {} 입니다.".format(a))
# else:
#     print("절대값은 {} 입니다.".format(-a))

# 함수
# 절대값 나타내는 함수: abs
# print("절대값은 {} 입니다.".format(abs(a)))


# 문제 5
# apple_p = 3000
# pear_p = 2000
# print("*** 사과: {}원 배: {}원 ***".format(apple_p,pear_p))
# apple = int(input("사과 개수: "))
# pear = int(input("배 개수: "))
# m = int(input("현재 소지 금액: "))
# total_p = apple_p * apple + pear_p * pear
# #  현금 - 총금액 0보다 큰 경우
# if m - total_p >= 0:
#     print("구매 가능. 잔액: {:,}원.".format(m - total_p))
# else:
#     print("구매 불가. 필요한 금액: {:,}원.".format(-(m - total_p)))
# 현금이 총금액보다 큰 경우 아닌 경우






# 문제 6
# a = int(input("수입력: "))
# if a % 15 == 0:
#     print("{}는 15의 배수 입니다.".format(a))
# elif a % 3 == 0:
#     print("{}는 3의 배수 입니다.".format(a))
# elif a % 5 == 0:
#         print("{}는 5의 배수 입니다.".format(a))
# else:
#     print("해당 조건 없음")


# 문제 7
# name = input("이름: ")
# height = float(input("키: "))
# weight = float(input("체중: "))
# n_weight = (height - 100) * 0.9
# weight_p = weight/(n_weight * 100)

# print("{}님의 비만도는 {:.2f}입니다.".format(name,weight_p))

# if weight_p < 100:
#     print("저체중")
# elif 100 <= weight_p < 110:
#     print("정상")
# elif 110 <= weight_p < 120:
#     print("과체중")
# elif 120 <= weight_p < 130:
#     print("비만")
# else:
#     print("고도 비만")

# 문제 8
# a = int(input("몇 일? "))
# if a % 4 == 1:
#     print("{}일. A가 청소 당번".format(a))
# elif a % 4 == 2:
#     print("{}일. B가 청소 당번".format(a))
# elif a % 4 == 3:
#     print("{}일. C가 청소 당번".format(a))
# else:
#     print("{}일. D가 청소 당번".format(a))

# 문제 9
# n = int(input("N일 후는 몇요일? "))
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
#     print("오늘은 화요일 입니다.")

# 문제 10
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# # 123
# r_a = a % 10 * 100 + a // 10 % 10 * 10 + a // 100
# r_b = b % 10 * 100 + b // 10 % 10 * 10 + b // 100

# if r_a > r_b:
#     print("큰 수: {}".format(r_a))
# elif r_a < r_b:
#     print("큰 수: {}".format(r_b))
# else:
#     print("두 수는 같습니다.")


# 문제 11
# 연도 = int(input("태어난 연도: "))
# if 연도 % 12 == 0:
#     print("태어난 연도: {}, 원숭이띠 입니다.".format(연도))
# elif 연도 % 12 == 1:
#     print("태어난 연도: {}, 닭띠 입니다.".format(연도))
# elif 연도 % 12 == 2:
#     print("태어난 연도: {}, 개띠 입니다.".format(연도))
# elif 연도 % 12 == 3:
#     print("태어난 연도: {}, 돼지띠 입니다.".format(연도))
# elif 연도 % 12 == 4:
#     print("태어난 연도: {}, 쥐띠 입니다.".format(연도))
# elif 연도 % 12 == 5:
#     print("태어난 연도: {}, 소띠 입니다.".format(연도))
# elif 연도 % 12 == 6:
#     print("태어난 연도: {}, 범띠 입니다.".format(연도))
# elif 연도 % 12 == 7:
#     print("태어난 연도: {}, 토끼띠 입니다.".format(연도))
# elif 연도 % 12 == 8:
#     print("태어난 연도: {}, 용띠 입니다.".format(연도))
# elif 연도 % 12 == 9:
#     print("태어난 연도: {}, 뱀띠 입니다.".format(연도))
# elif 연도 % 12 == 10:
#     print("태어난 연도: {}, 말띠 입니다.".format(연도))
# elif 연도 % 12 == 11:
#     print("태어난 연도: {}, 양띠 입니다.".format(연도))

# 문제 12
# 확실한 조건 부터 정리
# y = int(input("년도: "))
# if y % 400 == 0:
#     print("{}년 > 윤년".format(y))
# elif y % 100 == 0:
#     print("{}년 > 평년".format(y))
# elif y % 4 == 0:
#     print("{}년 > 윤년".format(y))
# else:
#     print("{}년 > 평년".format(y))

# y =int(input("년도: "))
# if y % 4 == 0 and y % 400 == 0:
#     print("{}년 > 윤년".format(y))
#     if y % 100 == 0:
#         print("{}년 > 평년".format(y))

# 중첩 if문 사용
y = int(input("년도: "))
if y % 4 == 0 and y % 100 != 0:
    if y % 400 == 0:
        print("{}년 > 윤년".format(y))
else:
    print("{}년 > 평년".format(y))
    