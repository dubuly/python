# i = 0
# while i < 5:
#     i += 1
#     j = 0
#     while j < 10:
#         print("*",end=" ")
#         j += 1
#     print()

# from random import random
# for i in range(6):
#     print(int(random()*45)+1)

# from random import random
# print((int(random()*50)+1)*2)

# from random import random
# print((int(random()*50)+1)*2-1)

# from random import random
# for i in range(6):
#     print(int(random()*100)+1)

# from random import randrange
# print(randrange(2,101,2))

# from random import random
# while True:
#     a = int((random()*100)+1)
#     print(a)
#     if a == 50:
#         print("반복 종료")
#         break

# from random import random
# for i in range(3):
#     a = int((random()*15)+1)
#     b = int((random()*15)+1)
#     c = int((random()*15)+1)
#     if a != b and b != c and c != a:
#         print(a,b,c)
#         break

# 문제 1
# from random import randrange
# r = randrange(1,11)
# print(r)
# a = int(input("수입력: "))


# while True:
#     if r < a:
#         print("UP")
#     elif r > a:
#         print("DOWN")
#     else:
#         print("GOOD")
#     break

# 문제 2
# from random import randrange
# r = randrange(1,11)
# print(r)

# for i in range(3):
#     a = int(input("수입력: "))

#     if r < a:
#         print("UP")
#     elif r > a:
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

#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
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

#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
#     else:
#         print("GOOD")
#         break
#     b -= 1

# 문제 5

# from random import randrange
# r = randrange(1,11)
# print(r)
# b = 0

# while True:
#     b += 1
#     a = int(input("수입력: "))

#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
#     else:
#         print("GOOD")
#         break

# print("{}번 만에 맞춤".format(b))

# 문제 6
# from random import randrange
# press = int(input("난이도 설정\n1:easy [1~10]\n2:normal [1~100]\n3:hard [1~1000]\n\n선택: "))

# if press == 1:
#     r = randrange(1,11)
#     print(r)
#     b = 0

#     while True:
#         b += 1
#         a = int(input("수입력: "))

#         if r < a:
#             print("DOWN")
#         elif r > a:
#             print("UP")
#         else:
#             print("GOOD")
#             break

#     print("{}번 만에 맞춤".format(b))

# elif press == 2:
#     r = randrange(1,101)
#     print(r)
#     b = 0

#     while True:
#         b += 1
#         a = int(input("수입력: "))

#         if r < a:
#             print("DOWN")
#         elif r > a:
#             print("UP")
#         else:
#             print("GOOD")
#             break

#     print("{}번 만에 맞춤".format(b))


# elif press == 3:
#     r = randrange(1,1001)
#     print(r)
#     b = 0

#     while True:
#         b += 1
#         a = int(input("수입력: "))

#         if r < a:
#             print("DOWN")
#         elif r > a:
#             print("UP")
#         else:
#             print("GOOD")
#             break

#     print("{}번 만에 맞춤".format(b))

# else:
#     print("잘못입력하셨습니다")
    
# from random import randrange
# press = int(input("난이도 설정\n1:easy [1~10]\n2:normal [1~100]\n3:hard [1~1000]\n\n선택: "))

# if press == 1:
#     r = randrange(1,11)

# elif press == 2:
#     r = randrange(1,101)

# elif press == 3:
#     r = randrange(1,1001)

# else:
#     print("잘못입력하셨습니다")

# print(r)
# b = 0

# while True:
#     b += 1
#     a = int(input("수입력: "))

#     if r < a:
#             print("DOWN")
#     elif r > a:
#             print("UP")
#     else:
#             print("GOOD")
#             break
# print("{}번 만에 맞춤".format(b))

# from random import randrange
# r = randrange(1,100)
# print(r)

# while True:
#     if r % 2 == 0:
#         print("True")
#     else:
#         print("False")
#     break

# from random import random
# r = int((random()*99)+1)
# print(r)

# while True:
#     if r % 2 == 0:
#         print("True")
#     else:
#         print("False")
#     break

# from random import random
# print(int(random()*10)+1)

# from random import random
# for i in range(6):
#     print(int(random()*45)+1)

# from random import random
# print((int(random()*50)+1)*2)

# from random import random
# print((int(random()*50)+1-2))


# from random import randrange
# print(randrange(2,100,2))
# print(randrange(1,100,2))

# from random import random
# for i in range(6):
#     print(int(random()*100)+1)

# from random import random
# while True:
#     r = int((random()*100)+1)
#     print(r)

#     if r == 50:
#         print("반복 종료")
#         break

# from random import random
# a = int((random()*15)+1)
# b = int((random()*15)+1)
# c = int((random()*15)+1)

# for i in range(3):
#     if a != b and b != c and c != a:
#         print(a,b,c)
#         break

# from random import randrange
# r = randrange(1,11)
# print(r)
# a = int(input("수입력: "))

# while True:
#     if r < a:
#         print("UP")
#     elif r > a:
#         print("DOWN")
#     else:
#         print("GOOD")
#     break

# from random import randrange
# r = randrange(1,11)
# print(r)

# for i in range(3):
#     a = int(input("수입력: "))

#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
#     else:
#         print("GOOD")
# break

# from random import randrange
# r = randrange(1,11)
# print(r)

# while True:
#     a = int(input("수입력: "))

#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
#     else:
#         print("GOOD")
#         break


# from random import randrange
# r = randrange(1,11)
# print(r)
# b = 3

# for i in range(3):
#     print("체력: {}".format(b))
#     a = int(input("수입력: "))

#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
#     else:
#         print("GOOD")
#         break
#     b -= 1

# from random import randrange
# r = randrange(1,11)
# print(r)
# b = 0

# while True:
#     a = int(input("수입력: "))
#     b += 1
#     if r < a:
#         print("DOWN")
#     elif r > a:
#         print("UP")
#     else:
#         print("GOOD")
#         break

# print("시도 횟수: {}".format(b))

# from random import randrange
# press = int(input("난이도 설정\n1:easy[1~10]\n2:normal [1~100]\n3:hard [1~1000]\n\n선택: "))

# if press == 1:
#     r = randrange(1,11)

# elif press == 2:
#     r = randrange(1,101)

# elif press == 3:
#     r = randrange(1,1001)
    
#     print(r)
#     b = 0

#     while True:
#         a = int(input("수입력: "))
#         b += 1
        
#         if r < a:
#             print("DOWN")
#         elif r > a:
#             print("UP")
#         else:
#             print("GOOD")
#             break

#     print("시도 횟수: {}".format(b))


# from random import random
# a = int((random()*100)+1)
# print(a)

# while True:
#     if a % 2 == 0:
#         print("TRUE")
#     else:
#         print("FALSE")
#     break

# from random import randrange
# a = randrange(1,101)
# print(a)

# while True:
#     if a % 2 == 0:
#         print("TRUE")
#     else:
#         print("FALSE")
#     break

# for i in range(5):
#     for j in range(1,6):
#         print(j+5*i,end=" ")
#     print()


# a = int(input("시작값: "))
# b = int(input("끝값: "))
# c = int(input("증가값: "))
# for i in range(a,b+1,c):
#     if i % 7 == 0:
#         print(i)
# sum = 0
# sum1 = 0
# for i in range(1,101):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             sum += i
#             sum1 += 1
# print("합: {} 개수: {}".format(sum,sum1))


# a = int(input("수입력: "))
# b = int(input("수입력: "))
# sum = 0


# if a < b:
#     for i in range(a,b+1):
#         sum += i
#     print("합: {}".format(sum))

# elif a > b:
#     for i in range(b,a+1):
#         sum += i
#     print("합: {}".format(sum))
# else:
#     print("두 수는 같다")

# 문제 8
# won = 10
# sum = 0
# for i in range(1,31):
    
#     sum += won
#     won *= 2

# print("총금액: {:,}원".format(sum))

# import turtle
# import turtle as t
# a = int(input("몇각형? "))
# for i in range(1,a+1):
#     t.forward(100)
#     t.left(360/a)
# t.mainloop()

# for i in range(3):
#     print("첫번째 for문")
#     for j in range(2):
#         print("두번째 for문")

# for i in range(3):
#     for j in range(3):
#         print("이중 for문 (i: {}\tj: {})".format(i,j))

# for i in range(2,10):
#     for j in range(1,10):
#         print("{} x {} = {}".format(i,j,i*j),end=" ")
#     print()


# for i in range(1,10):
#     for j in range(2,10):
#         print("{} x {} = {}".format(j,i,j*i),end="\t")
#     print()


# a = b = c = d = e = 0
# for i in range(5):
#     print("상위 for문 {}일때 하위 for문".format(i),end=":")
#     for j in range(1):
#         print("{}{}{}{}{}".format(a,b,c,d,e))
#         b += 1
#         c += 2
#         d += 3
#         e += 4

# for i in range(1,22,5):
#     print(i)
# for j in range(5):
#     print(j)

#         print(i+j,end="\t")
#     print()

# a = 0
# for i in range(5):
#     for j in range(5):
#         a += 1
#         print(a,end="\t")
#     print()


# for i in range(5):
#     for j in range(1,6):
#         print(j+5*i,end=" ")
#     print()
# sum = 0
# sum1 = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         sum += i
#     if i % 2 == 1:
#         sum1 += i
# print("짝수합: {} 홀수합: {}".format(sum,sum1))

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print(i)

# i = 1
# a = True
# while a:
#     print(i)

#     if i == 10:
#         a = False
#     i += 1


    # a = True

    # i = 1


    # while a:
    #     print(i)

    # if i == 10:
    #     a = False

    # i += 1

# while True:
#     m = int(input("몇월? "))
#     if 1 <= m <= 12:
#         if 1 <= m <= 3:
#             print("봄")
#         elif 4 <= m <= 6:
#             print("여름")
#         elif 7 <= m <= 9:
#             print("가을")
#         elif 10 <= m <= 12:
#             print("겨울")
#             print("반복종료")
#             break
#     else:
#         print("다시 입력하세요")
#         continue
#     break


# for i in range(1,6):
#     print(i)
# j = 1
# while j < 6:
#     print(j)
#     j += 1

# from random import randrange

# while True:
#     r = int((randrange(1,101)))
#     print(r)
#     if r == 50:
#         break


# for i in range(1,11):
#     for j in range(1):
#         print("*"*i)

# for i in range(1,11):
#     for j in range(1):
#         print(" "*(10-i)+"*"*i)

# y = 2022
# m = 9
# d = 28
# print(y,m,d,sep="/")


# for i in range(1,11):
#     for j in range(1):
#         print(" "*(10-i),"*"*((2*i)-1),sep="")

# for i in range(11,0,-1):
#     for j in range(1):
#         print("*"*i)

# for i in range(11,0,-1):
#     for j in range(1):
#         print(" "*(11-i),"*"*i)

# for i in range(1,11):
#     for j in range(1):
#         print("*"*(i-1)," "*((2*i)-1),sep="")

# for i in range(1,6):
#     print(" "*(5-i),"*"*i)

# for i in range(1,6):
#     print(" "*(i)+"*"*(6-i))

# for i in range(1,11):
#     print(" "*(i-1)+"*"*(21-(2*i)))

# for i in range(1,10):
#     for j in range(1):
#         print(" "*(10-i),"*"*((i*2)-1),sep="")

# for i in range(1,11):
#     for j in range(1):
#         print(" "*((i-1)),"*"*(21-(i*2)),sep="")
