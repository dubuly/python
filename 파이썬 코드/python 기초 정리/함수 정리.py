# 문제1

# def 함수1():
#     print("안녕하세요")
# 함수1()

# 문제 2

# def 함수2(a):
#     if a % 2 == 0:
#         return "{}는 짝수".format(a)
#     else:
#         return "{}는 홀수".format(a)
    
# a = int(input("수입력: "))

# print(함수2(a))

# 문제 3

# a = int(input("수입력: "))
# b = int(input("수입력: "))

# def 함수3(a,b):
#     return "합: {}".format(a+b)

# print(함수3(a,b))

# 문제 4

# def 함수4(a):
#     if a % 7 == 0:
#         return "{}는 7의 배수".format(a)
#     else:
#         return "{}는 7의 배수가 아니다".format(a)

# a = int(input("수입력: "))

# print(함수4(a))

# 문제 5

# def 함수5(a):

#     r_a = ""
#     for i in a:
#         r_a = i + r_a
#     return r_a

# a = input("문자 입력: ")

# print(함수5(a))


# 약수 구하기

# def 약수(a):
#     for i in range(1,a+1):
#         if a % i == 0:
#             print("{}는 약수".format(i))
# 약수(8)


# def 약수(a):
#     b = []
#     for i in range(1,a+1):
#         if a % i == 0:
#             b.append(i)
#     return b
# print(약수(8))

# 튜플
# tuple = (10,20,30)
# print(tuple[0],tuple[1],tuple[2])

# a,b = (10,20)

# print("요소 교환 전: {}\t{}".format(a,b))

# a,b = b,a

# print("요소 교환 전: {}\t{}".format(a,b))


# def test():
#     return (10,20)

# a,b = test()

# print(a)
# print(b)
# print(test())


# a = int(input("정수 입력: "))
# b = a % 10

# if b == 0 or b == 2 or b == 4 or b == 6 or b == 8:
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 홀수".format(a))

# a = int(input("수입력: "))

# if a % 2 == 0:
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 홀수".format(a))

# a = int(input("수입력: "))

# if a % 3 == 0:
#     print("{}는 3의 배수".format(a))
# else:
#     print("{}는 3의 배수가 아니다".format(a))


# a = int(input("수입력: "))
# b = int(input("수입력: "))

# if a > b:
#     print("{}는 {}보다 큰 수".format(a,b))
# else:
#     print("{}는 {}보다 큰 수".format(b,a))


# a = int(input("수입력: "))
# if a == 1:
#     print("{} 입니다".format(a))
# elif a == 2:
#     print("{} 입니다".format(a))
# elif a == 3:
#     print("{} 입니다".format(a))
# elif a == 4:
#     print("{} 입니다".format(a))
# else:
#     print("잘못입력하셨습니다")

# for i in range(11):
#     print("문자열")

# for i in range(10,0,-1):
#     print(i)

# for i in range(10,0,-1):
#     print("문자열",i)


# st = "string"
# for i in st:
#     print(i)


# sum1 = 0
# for i in range(1,11):
#     sum1 += i
# print(sum1)

# a = int(input("시작값: "))
# b = int(input("끝값: "))
# c = int(input("증가값: "))

# sum1 = 0
# for i in range(a,b+1,c):
#     sum1 += i
# print(sum1)

    
# for i in range(1,31):
#     print(i,end="\t")
#     if i % 5 == 0:
#         print()

# st = "It is a fun Python class"
# a = 0
# s = 0
# for i in st:
    
#     if i == "a":
#         a += 1
#     elif i == "s":
#         s += 1
# print("a의 개수: {}\ns의 개수: {}".format(a,s))

# a = int(input("수입력: "))
# sum1 = 0
# sum2 = 0
# for i in range(1,a+1):
#     if i % 2 == 0:
#         sum1 += i
#     else:
#         sum2 += i
# print("짝수의 합: {}\n홀수의 합: {}".format(sum1,sum2))

# a = 10
# sum1 = 0

# for i in range(1,31):
#     sum1 += a
#     a *= 2

# print("예금액: {:,}".format(sum1))

# for i in range(3):
#     print("첫번째 for문")
#     for j in range(2):
#         print("두번째 for문")


# for i in range(3):
#     for j in range(3):
#         print("이중 for 문(i:{}\t\t\tj:{})".format(i,j))


# for i in range(2,10):
#     for j in range(1,10):
#         print("{} x {} = {}".format(i,j,i*j),end="\t")
#     print()

# for i in range(1,10):
#     for j in range(2,10):
#         print("{} x {} = {}".format(j,i,i*j),end="\t")
#     print()

# a = 0
# b = 0

# i = 1
# while i < 11:
#     if i % 2 == 0:
#         a += i
#     else:
#         b += i
#     i += 1
# print("짝수 합: {} 홀수 합: {}".format(a,b))


# i = 0

# while i < 6:
#     print(i)
#     i += 1

# i = 1
# while True:
#     if i < 11:
#         print(i)
#         i += 1

# while True:
#     a = int(input("몇월? "))

#     if 1 <= a <= 3:
#         print("{}는 봄입니다".format(a))
#     elif 4 <= a <= 6:
#         print("{}는 여름입니다".format(a))
#     elif 7 <= a <= 9:
#         print("{}는 가을입니다".format(a))
#     elif 9 <= a <= 12:
#         print("{}는 겨울입니다".format(a))
        
#     else:
#         print("잘못입력하셨습니다")
#         continue
#     break
# print("반복 종료")

# from random import random

# # while True:
# #     r = int(random()*100)+1
# #     print(r)
# #     if r == 50:
# #         break

# a = int(random()*15)+1
# b = int(random()*15)+1
# c = int(random()*15)+1

# while True:
#     if a != b and b != c and c !=a:
#         print("{}\t{}\t{}".format(a,b,c))
#         break


# a = [0,0,0]

# a[0] = int(input("수입력: "))
# a[1] = int(input("수입력: "))
# a[2] = int(input("수입력: "))

# total = a[0]+a[1]+a[2]

# print(total)

# 과일 = ["사과","귤","자두","포도"]

# 과일[0] = "복숭아"
# print(과일)


a = input("문자 입력: ")
b = a[-1]

if b in "24680":
    print("{}는 짝수".format(a))
