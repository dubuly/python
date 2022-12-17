# 문제 1

# n = int(input("수입력: "))

# if n % 2 == 0:
#     print("{}는 짝수".format(n))
# else:
#     print("{}는 홀수".format(n))


# 문제 2

# n = int(input("수입력: "))

# for i in range(1,n+1):
#     if i % 2 == 0:
#         print("{}는 짝수".format(i))
#     else:
#         print("{}는 홀수".format(i))


# 문제 3

# n = int(input("수입력: "))
# sum1 = 0
# sum2 = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum1 += i
#     else:
#         sum2 += i
# print("짝수의 합: {}\t홀수의 합: {}".format(sum1,sum2))


# 문제 4

# n = int(input("수입력: "))
# b = []
# b.append(n)
# print(b)


# 문제 5
# a = []
# n = int(input("수입력: "))

# for i in range(1,n+1):
#     a.append(i)
# print(a)



# 문제 6

# n = int(input("수입력: "))
# b = []

# for i in range(1,n+1):
#     if i % 2 == 1:
#         b.append(i)
# print(b)


# 문제 7

# n = int(input("수입력: "))

# if n % 3 == 0:
#     print("{}는 3의 배수".format(n))
# else:
#     print("{}는 3의 배수가 아닙니다".format(n))


# 문제 8

# n = int(input("수입력: "))

# for i in range(1,n+1):
#     if i % 3 == 0:
#         print("{}는 3의 배수".format(i))
#     else:
#         print("{}는 3의 배수가 아니다".format(i))


# 문제 9

# n = int(input("몇일? "))

# if n % 4 == 0:
#     print("{}일 청소 당번: D".format(n))
# elif n % 4 == 1:
#     print("{}일 청소 당번: A".format(n))
# elif n % 4 == 2:
#     print("{}일 청소 당번: B".format(n))
# elif n % 4 == 3:
#     print("{}일 청소 당번: C".format(n))



# 문제 10

# n = int(input("몇일? "))

# for i in range(1,n+1):
#         if i % 4 == 0:
#             print("{}일 청소 당번: D".format(i))
#         elif i % 4 == 1:
#             print("{}일 청소 당번: A".format(i))
#         elif i % 4 == 2:
#             print("{}일 청소 당번: B".format(i))
#         elif i % 4 == 3:
#             print("{}일 청소 당번: C".format(i))


# 문제 11

# n = int(input("몇년도? "))

# if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
#     print("{}는 윤년".format(n))
# else:
#     print("{}는 평년".format(n))


# 문제 12

# n = int(input("몇년도? "))
# b = []

# for i in range(1,n+1):
#     if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
#         b.append(i)
# print("윤년인 년도: {}".format(b))


# 문제 13

# a = int(input("수입력: "))
# for i in range(1):
#     if a % 2 == 0:
#         print("{}는 짝수".format(a))
#     else:
#         print("{}는 홀수".format(a))

#     b = int(input("수입력: "))
#     if b % 2 == 0:
#         print("{}는 짝수".format(b))
#     else:
#         print("{}는 홀수".format(b))

#     c = int(input("수입력: "))
#     if c % 2 == 0:
#         print("{}는 짝수".format(c))
#     else:
#         print("{}는 홀수".format(c))

#     d = int(input("수입력: "))
#     if d % 2 == 0:
#         print("{}는 짝수".format(d))
#     else:
#         print("{}는 홀수".format(d))


# 문제 14

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# d = int(input("수입력: "))

# for i in range(1):
#     if a % 2 == 0:
#         print("{}는 짝수".format(a))
#     else:
#         print("{}는 홀수".format(a))

#     if b % 2 == 0:
#         print("{}는 짝수".format(b))
#     else:
#         print("{}는 홀수".format(b))

#     if c % 2 == 0:
#         print("{}는 짝수".format(c))
#     else:
#         print("{}는 홀수".format(c))

#     if d % 2 == 0:
#         print("{}는 짝수".format(d))
#     else:
#         print("{}는 홀수".format(d))


# 문제 15

# a = int(input("수입력: "))
# b = int(input("수입력: "))

# for i in range(1):
#     if a % 10 + b % 10 > 9:
#         print("합: {}\t받아올림 발생".format(a+b))
#     else:
#         print("받아올림 발생 x")


# 문제 16

# i = 0
# while True:
#     a = int(input("수입력: "))
#     b = int(input("수입력: "))

#     if a % 10 + b % 10 > 9:
#         print("합: {}\t받아올림 발생".format(a+b))
#     else:
#         print("받아올림 발생 x")
#         i += 1

#     if i == 5:
#         break


# 문제 17

# a = int(input("점수: "))
# b = int(input("점수: "))
# c = int(input("점수: "))
# d = int(input("점수: "))
# e = int(input("점수: "))
# avr = (a+b+c+d+e)/5


# print("평균: {}".format(avr))


# 문제 18

# a = int(input("점수: "))
# b = int(input("점수: "))
# c = int(input("점수: "))
# d = int(input("점수: "))
# e = int(input("점수: "))
# avr = (a+b+c+d+e)/5

# print("평균: {}".format(avr))

# if a < avr:
#     print("{}는 평균 이하".format(a))
# if b < avr:
#     print("{}는 평균 이하".format(b))
# if c < avr:
#     print("{}는 평균 이하".format(c))
# if d < avr:
#     print("{}는 평균 이하".format(d))
# if e < avr:
#     print("{}는 평균 이하".format(a))


# 문제 19

# a = float(input("수입력: "))
# b = float(input("수입력: "))

# if a % 10 > 4:
#     print("{:.1f} 반올림 발생".format(a))
# if b % 10 > 4:
#     print("{:.1f}는 반올림 발생".format(b))
# else:
#     print("반올림 발생 x")


# 문제 20
# i = 1
# while True:

#     a = float(input("수입력: "))
#     b = float(input("수입력: "))

#     if a % 10 > 4:
#         print("{:.1f}는 반올림 발생".format(a))
#     if b % 10 > 4:
#         print("{:.1f}는 반올림 발생".format(b))
#     else:
#         print("반올림 발생 x")

#         i += 1
#     if i == 5:
#         break


# 문제 22

login = ("admin","12345")

id = input("관리자 아이디를 입력하세요: ")
pw = input("관리자 비밀번호를 입력하세요: ")

if id == login[0] and pw == login[1]:
    print("관리자 계정으로 로그인에 성공하셨습니다.")
else:
    print("아이디 또는 비밀번호가 잘못 입력되었습니다.")


# 문제 23

# dict = {"아이디":"admin","비밀번호":12345}

# id = input("관리자 아이디를 입력하세요: ")
# pw = input("관리자 비밀번호를 입력하세요: ")

# if dict["아이디"] in "admin" and dict["비밀번호"] in 12345:
#     print("관리자 계정으로 로그인에 성공하셨습니다")
