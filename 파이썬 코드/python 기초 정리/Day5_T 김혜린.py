# # 문제6
# print("섭씨온도를 화시온도로 바꿔드립니다!!")
# 섭씨온도 = int(input("섭씨온도를 입력해주세요: "))
# 화씨온도 = 섭씨온도 * 1.8 + 32
# print("섭씨온도 : {} > 화씨온도 : {}".format(섭씨온도, 화씨온도))


# # 문제7 

# # 신장: 180 체중 : 90 bmi : 27.777777777778
# # bmi = 몸무게(kg) / (신장(m) * 신장(m))

# h = float(input("키: "))
# w = float(input("몸무게: "))
# h1 = h / 100

# bmi = w / (h1 * h1)

# print("bmi 지수 : {:.2f}".format(bmi))

# # 문제8 
# # 입력 : 123

# # 일자리 : 3
# # 십자리 : 23
# # 백자리 : 123

# a = int(input("세자리 수 입력: "))

# a1 = a - int(a/10)*10 # 123 - 120 = 3
# a2 = a - int(a/100)*100 # 123 - 100 = 23
# a3 = a # 123

# print("일: {}\n십: {} \n백: {}".format(a1,a2,a3))


# #예제1

# print("9999를 14로 나누었을 때의")
# print("몫: {}".format(9999/14))
# print("나머지: {}".format(9999%14))


# print("9999를 14로 나누었을 때의")
# print("몫: {}".format(9999//14))
# print("나머지: {}".format(9999%14))



# print(3/2)

# print(3//2)

# print(3%2)



# 문제8 
# 입력 : 123

# 일자리 : 3
# 십자리 : 23
# 백자리 : 123

# a = int(input("세자리 수 입력: "))

# a1 = a%10 
# a2 = a%100 
# a3 = a%1000 

# print("일: {}\n십: {} \n백: {}".format(a1,a2,a3))


# # 문제9
# # 입력 : 123

# # 일자리 : 3
# # 십자리 : 2
# # 백자리 : 1

# a = int(input("세자리 수 입력: "))

# a1 = a%10
# a2 = a%100//10
# a3 = a%1000//100

# print("일: {}\n십: {} \n백: {}".format(a1,a2,a3))



# #문제10

# year = int(input("생년월일 8자리를 입력해주세요: "))

# # 20220913

# y = year // 10000
# m = year  % 10000 // 100
# d = year % 100

# print("년: {}\n월: {}\n일: {}".format(y,m,d))


# #문제11

# year = int(input("생년월일 6자리를 입력해주세요: "))

# # 220913

# y = year // 10000
# m = year  % 10000 // 100
# d = year % 100

# print("년: {}\n월: {}\n일: {}".format(y,m,d))


# # 문제12

# # 01234|56789

# # 예시
# # 01234
# # 56789

# a = int(input("10자리 정수 입력: "))

# b = a // 100000
# c = a % 100000

# print(b)
# print(c)

# # 11111112172382738732812790309


# # turtle (그래픽 모듈)

# # 호출
# import turtle

# # 모양 설정
# turtle.shape("turtle")

# # 이동
# turtle.forward(100)

# # 유지
# turtle.mainloop()


# # 예제1
# import turtle

# turtle.left(90)

# turtle.forward(100)

# turtle.mainloop()

# # 예제2

# import turtle as t

# t.left(120)
# t.forward(100)

# t.left(120)
# t.forward(100)

# t.left(120)
# t.forward(100)

# t.mainloop()


# # 문제1

# import turtle as t

# a = int(input("길이 입력: "))

# t. shape("circle")

# t.left(120)
# t.forward(a)

# t.left(120)
# t.forward(a)

# t.left(120)
# t.forward(a)

# t.mainloop()

# # 문제2

# import turtle as t

# a = int(input("세로 길이 입력: "))
# b = int(input("가로 길이 입력: "))

# t. shape("circle")

# t.left(90)
# t.forward(a)

# t.left(90)
# t.forward(b)

# t.left(90)
# t.forward(a)

# t.left(90)
# t.forward(b)

# t.mainloop()

# # 문제3

# import turtle as t

# a = int(input("길이 입력: "))

# t. shape("circle")

# t.left(60)
# t.forward(a)

# t.left(60)
# t.forward(a)

# t.left(60)
# t.forward(a)

# t.left(60)
# t.forward(a)

# t.left(60)
# t.forward(a)

# t.left(60)
# t.forward(a)

# t.mainloop()