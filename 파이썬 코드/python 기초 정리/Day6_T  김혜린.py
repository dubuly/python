# # 문제4

# import turtle as t

# a = int(input("길이 입력: "))

# t. shape("circle")

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


# # 추가

# import turtle as t

# a = int(input("길이 입력: "))

# t. shape("circle")

# #1회
# t.forward(a)
# t.right(144)
# t.forward(a)

# #2회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)

# #3회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)

# #4회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)

# #5회
# t.left(72)
# t.forward(a)
# t.right(144)
# t.forward(a)

# t.mainloop()

# # 실습
# import turtle as t

# t.shape('turtle')
# t.speed('fastest')  

# for i in range(360):  # 360번 반복
#     t.fd(i)
#     t.right(91)   

# t.mainloop()

# 제어문

# # 조건문

# print(True)

# print(False)

# x = 10
# y = 20

# print(x == y)
# print(x != y)


# #예제1

# x = 10
# y = 20

# # True
# print(not x == y)
# print(not x > y)
# print(not x >= y)


# # False
# print(not x != y)
# print(not x < y)
# print(not x <= y)

# # 예제1

# num = int(input("수입력: "))

# if num == 1:
#     print("1입니다.")

# : 미입력시 -> SyntaxError: expected ':'
# 들여쓰기 X -> IndentationError: expected an indented block after 'if' statement on line 113

# # 예제2

# if True:
#     print("True입니다.")

# if False:
#     print("False입니다.")


# # 문제1

# num = int(input("수입력: "))

# if num > 0:
#     print("{}은 양수 입니다.".format(num))

# if num < 0:
#     print("{}은 음수 입니다.".format(num))

# if num == 0:
#     print("0입니다.")


# 11111111111111111111111111111111111111111110
# 111111111111111111111111787878787
# 34567899090737908
# 7777777777777


# # 문제2

# a = int(input("수입력: "))

# b = a % 10

# # print(b)

# # 짝수
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

# # 홀수
# if b == 1:
#     print("{}은 홀수 입니다.".format(a))
# if b == 3:
#     print("{}은 홀수 입니다.".format(a))
# if b == 5:
#     print("{}은 홀수 입니다.".format(a))
# if b == 7:
#     print("{}은 홀수 입니다.".format(a))
# if b == 9:
#     print("{}은 홀수 입니다.".format(a))


# 문제3

num = int(input("수입력: "))

# #1번
# if num % 2 == 0:
#     print("{}은 짝수 입니다".format(num))

# if num % 2 != 0:
#     print("{}은 홀수 입니다.".format(num))

# #2번
# if num % 2 == 0:
#     print("{}은 짝수 입니다".format(num))

# if num % 2 == 1:
#     print("{}은 홀수 입니다.".format(num))



