# 문제 9
# i = 0
# while i < 5:
#     i += 1
#     j = 0 # j 초기값을 코드 안에 넣어주어야 함 
#     while j < 10:
#         print("*",end=" ")
#         j += 1
#     print()

# 호출 방법1

# import turtle
# turtle.forward()

# 호출 방법2(모든 함수 호츨/ 일일이 다 안 써도 됨)

# from turtle import forward
# forward()


# random 함수
# 임의의 값을 생성할 때 사용

# from random import random
# print(ramdom())
# -> 0.0 ~ 1.0 미만의 임의의 값 생성

# 0.0~ 10.0 미만의 임의의 값 생성
# from random import random
# print(random()*10)

# 0 ~ 10 미만의 임의의 값 생성 - > 실수형으로 변환
# from random import random
# print(int(random()*10))

# 1 ~ 10까지의 임의의 값 생성
# from random import random
# print(int(random()*10)+1)


# 1 ~ 45 까지의 임의의 값 6개 생성
# from random import random

# for i in range(6):
#     print(int(random()*45)+1)

# 1 ~ 100까지의 짝수 임의의값 생성
# from random import random

# print((int(random()*50)+1)*2)

# 1 ~ 100까지의 홀수 임의의값 생성
# from random import random

# print((int(random()*50)+1)*2-1)


# randrange()

# from random import randrange

# 짝수
# print(randrange(2,101,2))

# 홀수
# print(randrange(1,101,2))

# 문제 1
# from random import random
# for i in range(6):
#     print(int(random()*100)+1)

# 문제 2
# from random import random
# while True:
#     a = int(random()*100)+1
#     print(a)
#     if a == 50:
#         break
#     # print 함수는 출력해주는 함수이기 때문에 변수에 지정 x


# 문제 3
# from random import random
# while True:
#     a = int(random()*15)+1
#     b = int(random()*15)+1
#     c = int(random()*15)+1

#     if a != b and a != c and b != c:
#         print("{}\t{}\t{}".format(a,b,c,))
#         break

# 문제 1
# from random import randrange
# r = randrange(1,11)
# print(r)
# a = int(input("수입력: "))


# if a < r:
#     print("UP")
# elif a > r:
#     print("DOWN")
# else:
#     print("GOOD")


# 문제 2
# from random import randrange
# r = randrange(1,11)
# print(r)
# for i in range(3):
#     a = int(input("수입력: "))

#     if a < r:
#         print("UP")
#     elif a > r:
#         print("DOWN")
#     else:
#         print("GOOD")
#         break

# 문제 3
# from random import randrange
# r = randrange(1,11)
# print(r)
# while True:
#     a = int(input("수입력: "))

#     if a < r:
#         print("UP")
#     elif a > r:
#         print("DOWN")
#     else:
#         print("GOOD")
#         break

# 문제 4
# from random import randrange
# r = randrange(1,11)
# print(r)
# b = 3

# for i in range(3):
#     print("체력: {}".format(b))
#     a = int(input("수입력: "))

#     if a < r:
#         print("UP")
#     elif a > r:
#         print("DOWN")
#     else:
#         print("GOOD")
#         break

# 문제 5
# from random import randrange
# r = randrange
# print(r)
# b = 9

# while True:
#      a = int(input("수입력: "))
#      for i in range(r):
#         if a < r:
#             print("UP")
#         elif a > r:
#             print("DOWN")
#         else:
#             print("GOOD")
#             break

#  문제 5
# from random import randrange
# r = randrange(1,11)
# print(r)
# b = 0

# while True:
#     a = int(input("수입력: "))
#     b += r

#     if a < r:
#         print("UP")
#     elif a > r:
#         print("DOWN")
#     else:
#         print("GOOD")
#         break



# 문제 6
from random import randrange
press = int(input("난이도 설정\n1:easy: [1~10]\n2:normal: [1~100]\n3. hard: [1~1000]"))

if press == 1:

    r = randrange(1,11)
    print(r)

    b = 0

    while True:
        b += 1
        a = int(input("수입력: "))

        if a > r:
            print("DOWN")

        elif a < r:
            print("UP")

        else:
            print("GOOD")
            break
    print("{}번만에 맞춤.".format(b))

elif press == 2:

    r = randrange(1,101)
    print(r)

    b = 0

    while True:
        b += 1
        a = int(input("수입력: "))

        if a > r:
            print("DOWN")

        elif a < r:
            print("UP")

        else:
            print("GOOD")
            break
    print("{}번만에 맞춤.".format(b))

    if press == 3:

        print(r)

    b = 0

    while True:
        b += 1
        a = int(input("수입력: "))

        if a > r:
            print("DOWN")

        elif a < r:
            print("UP")

        else:
            print("GOOD")
            break
    print("{}번만에 맞춤.".format(b))
      