# 예제 6
# a = int(input("한 변의 길이: "))
# import turtle
# import turtle as t
# t.shape("turtle")
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)
# t.left(144)
# t.forward(a)

# t.mainloop()

# 추가 문제(별 그리기)
# a = int(input("힌 변의 길이: "))
# import turtle
# import turtle as t
# # t.shape("turtle")
# t.forward(a)
# t.right(144)
# t.forward(a)
# t.right(108)
# t.backward(a)
# t.right(144)
# t.backward(a)
# t.right(108)
# t.forward(a)
# t.right(144)
# t.forward(a)
# t.right(108)
# t.backward(a)
# t.right(144)
# t.backward(a)
# t.right(108)
# t.forward(a)
# t.right(144)
# t.forward(a)
# t.right(108)
# t.mainloop()

# a = int(input("힌 변의 길이: "))
# import turtle
# import turtle as t
# t.shape("turtle")
# # 1회
# t.forward(a)
# t.right(144)
# t.forward(a)
# # 2회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)
# # 3회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)
# # 4회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)
# # 5회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)

# t.mainloop()

# 아무거나 그려보기
# import turtle as t
# t.shape('turtle')
# t.speed('fastest')

# for i in range(360):  # 360번 반복
#     t.fd(i) # forward 약자
#     t.right(91)

# t.mainloop()

# 제어문

# 조건문

# True 출력(대문자로 출력!!!!!)
# print(True)
# # False 출력
# print(False)

# x = 10
# y = 20
# print(x == y) # (== : 같다)
# print(x != y) # (!= : 다르다)

# 비교 연산자
# 연산자         설명
#  ==           같다
#  !=           다르다

# print(10 == 100)
# print(10 != 100)
# print(10 > 100)
# print(10 < 100)
# print(10 >= 100)
# print(10 <= 100)

# 비교 연산자(문자열 -> 사전순으로 문자 대소 비교 가능, 뒤에 있을수록 큼
# (가 보다 하가 더 크다)
# print("가방"<"가방")
# print("가방">"하마")
# print("가방"<"하마")
# print("가방">"하마")

# 논리 연산자
# 연산자        설명
#  and          그리고
#  or           또는
# not           아니다

# 논리 연산자: not 연산자
# not 연산자는 참과 거짓을 반대로 바꿀때 사용
# print(not False)
# print(not True)

# 예제 1
# x = 10
# y = 20

# # True
# print(not x == y)
# print(x < y)
# print(not y < x)
# print(not x == y)
# # False
# print(not x != y)
# print(not x < y)
# print( x > y)
# print(x == y)

# and 연산자
# and 연산자는 양쪽 변의 값이 모두 참일때만 True를 결과로 낸다.

# or 연산자
# or 연산자는 둘(양쪽 변의 값)중 하나만 참이어도 True를 결과로 낸다.

# # 둘다 True 일때만 True(and)
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# # 하나라도 True 이면 True(or)
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# if 조건문
# 파이썬에서 if 조건문은 조건에 따라 코드를 실행하거나, 실행하지 않게 만들고 싶을 때 사용

# if 조건문 기본 구조
# if 조건식:
#      종속 문장
#      종속 문장
# 수행코드

# 예제 1
# a = int(input("정수 입력: "))

# if a == 1:
# print("1입니다.")

# : 미입력시 -> SyntaxError:  expected ':'
# 들여쓰기 x -> IndentationError/ 넣고 싶을때 tab/ 빼고 싶을때 shift + tab

# 예제 2
# if True:
#     print("True입니다.")
# if False:
#     print("False입니다.") # 주석처리(if 다음 False가 왔기 때문)

# 문제 1
# a = int(input("정수 입력: "))
# if a > 0:
#     print("{}은 양수 입니다.".format(a))
# if a < 0:
#     print("{}은 음수 입니다.".format(a))
# if a == 0:
#     print("0입니다.")

# 문제 2
# a = int(input("수입력: "))
# b = a % 10

# # print(b)

# if b == 0:
#     print("{}은 짝수 입니다.".format(a))
# if b == 2:
#     print("{}은 짝수 입니다.".format(a))
# if b == 4:
#     print("{}은 짝수 입니다.".format(a))
# if b == 6:
#     print("{}은 짝수 입니다.".format(a))
# if b == 8:
#     print("{}은 짝수 입니다.".format(a))

# 문제 3
a = int(input("수입력: "))

if a % 2 == 0:
    print("{}는 짝수 입니다.".format(a))
# if a % 2 != 0:
#     print("{}는 홀수 입니다.".format(a))

# or

if a % 1 == 0:
    print("{}는 홀수 입니다.".format(a))
