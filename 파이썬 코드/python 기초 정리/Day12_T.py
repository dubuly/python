# # 문제8

# for i in range(5):
#     for j in range(10):
#         print("*",end=" ")
#     print()


# # 문제9 (HW)

# i = 0
# while i < 5:
#     i += 1
#     j = 0
#     while j < 10:
#         print("*",end=" ")
#         j += 1
#     print()


# 모듈 호출

# 호출 방법1
# import turtle

# turtle.forward()

# # 호출방법2
# from turtle import forward

# forward()


# random 함수

# # 0.0 ~ 1.0미만의 임의의 값 생성

# # 호출1
# import random

# print(random.random())


# # 호출2
# from random import random

# print(random())


# # 0.0 ~ 10.0미만의 임의의 값 생성

# from random import random

# print(random()*10)


# # 0 ~ 10미만의 임의의 값 생성

# from random import random

# print(int(random()*10))


# # 1 ~ 10까지의 임의의 값 생성

# from random import random

# print(int(random()*10)+1)


# # 1 ~ 45까지의 임의의 값 6개 생성

# from random import random

# for i in range(6):
#     print(int(random()*45)+1)

# # 1 ~ 100까지의 짝수 임의의 값 생성
# from random import random

# print((int(random()*50)+1)*2)


# # 1 ~ 100까지의 홀수 임의의 값 생성
# from random import random

# print((int(random()*50)+1)*2-1)


# # randrange()

# from random import randrange

# # 짝수
# print(randrange(2,101,2))

# # 홀수
# print(randrange(1,101,2))



# # 문제1
# from random import random

# for i in range(6):
#     print(int(random()*100)+1)


# # 문제2

# from random import random

# while True:
#     rand = int(random()*100)+1
#     print(rand)
#     if rand == 50:
#         break

# # 문제3
# from random import random

# while True:
#     a = int(random()*15)+1
#     b = int(random()*15)+1
#     c = int(random()*15)+1

#     if a != b and a != c and b != c:
#         print("{}\t{}\t{}".format(a,b,c))
#         break


# up down game

# # 문제1
# from random import randrange

# r = randrange(1,11)
# print(r)
# a = int(input("수입력: "))

# if a > r:
#     print("DOWN!")

# elif a < r:
#     print("UP!")

# else:
#     print("GOOD!")


# # 문제2
# from random import randrange

# r = randrange(1,11)
# print(r)

# for i in range(3):
#     a = int(input("수입력: "))

#     if a > r:
#         print("DOWN!")

#     elif a < r:
#         print("UP!")

#     else:
#         print("GOOD!")
#         break


# # 문제3
# from random import randrange

# r = randrange(1,11)
# print(r)

# while True:
#     a = int(input("수입력: "))

#     if a > r:
#         print("DOWN!")

#     elif a < r:
#         print("UP!")

#     else:
#         print("GOOD!")
#         break


# # 문제4
# from random import randrange

# r = randrange(1,11)
# print(r)
# b = 3

# for i in range(3):
#     print("체력: {}".format(b))
#     a = int(input("수입력: "))

#     if a > r:
#         print("DOWN!")

#     elif a < r:
#         print("UP!")

#     else:
#         print("GOOD!")
#         break

#     b -= 1


# # 문제5
# from random import randrange

# r = randrange(1,11)
# print(r)

# b = 0

# while True:
#     b += 1
#     a = int(input("수입력: "))

#     if a > r:
#         print("DOWN!")

#     elif a < r:
#         print("UP!")

#     else:
#         print("GOOD!")
#         break
# print("{}번 만에 맞춤".format(b))


# # 문제6
# from random import randrange

# press = int(input("난이도 설정\n1:easy [1~10]\n2:normal [1~100]\n3:hard [1~1000]\n\n선택: "))

# if press == 1:

#     r = randrange(1,11)
#     print(r)

#     b = 0

#     while True:
#         b += 1
#         a = int(input("수입력: "))

#         if a > r:
#             print("DOWN!")

#         elif a < r:
#             print("UP!")

#         else:
#             print("GOOD!")
#             break
#     print("{}번 만에 맞춤".format(b))

# elif press == 2:

#     r = randrange(1,101)
#     print(r)

#     b = 0

#     while True:
#         b += 1
#         a = int(input("수입력: "))

#         if a > r:
#             print("DOWN!")

#         elif a < r:
#             print("UP!")

#         else:
#             print("GOOD!")
#             break
#     print("{}번 만에 맞춤".format(b))

# elif press == 3:

#     r = randrange(1,1001)
#     print(r)

#     b = 0

#     while True:
#         b += 1
#         a = int(input("수입력: "))

#         if a > r:
#             print("DOWN!")

#         elif a < r:
#             print("UP!")

#         else:
#             print("GOOD!")
#             break
#     print("{}번 만에 맞춤".format(b))

# else:
#     print("잘못입력하셨습니다.")


# # 문제7,8
from random import randrange

press = int(input("난이도 설정\n1:easy [1~10]\n2:normal [1~100]\n3:hard [1~1000]\n\n선택: "))

if press == 1:
    r = randrange(1,11)

elif press == 2:
    r = randrange(1,101)

elif press == 3:
    r = randrange(1,1001)

else:
    print("잘못입력하셨습니다.")

print(r)

b = 0

while True:
    b += 1
    a = int(input("수입력: "))

    if a > r:
        print("DOWN!")

    elif a < r:
        print("UP!")

    else:
        print("GOOD!")
        break
print("{}번 만에 맞춤".format(b))