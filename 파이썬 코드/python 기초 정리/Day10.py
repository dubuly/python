# s = int(input("시작값: "))
# e = int(input("끝값: "))
# g = int(input("증가값: "))
# for i in range(s,e+1,g):
#     if i % 7 == 0:
#         print("7의 배수: {}".format(i))
# sum = 0
# for i in range(1,101):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             sum += i
# print(sum)
# sum = 0
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# for i in range(a,b+1):
#     sum += i
# print(sum)

# sum = 0
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# if a < b:
#     for i in range(a,b+1):
#         sum += i
#         print(sum)
# elif a > b:
#     for i in range(b,a+1):
#         sum += i
#         print(sum)
# else:
#     print("두 수는 같다")

# won = 10
# sum = 0

# for i in range(1,31):
#     sum += won
#     won *= 2

# print("예금액: {:,}원".format(sum))


# won = 10

# sum1 = 0

# for i in range(1,31):

#     sum1 += won

#     won *= 2

# print("예금액: {:,}원".format(sum1))
# n = int(input("몇각형? "))
# import turtle
# import turtle as t
# for i in range(1,n+1):
#     t.forward(100)
#     t.left(360/n)
#     t.mainloop

# for i in range(3):
#     print("첫 번째 for문")
#     for i in range(2):
#         print("두번째 for문")

# for i in range(0,3):
#     for j in range(0,3):
#         print("이중 for 문 (i : {}\tj: {})".format(i,j))

# for i in range(2,10):
#     for j in range(1,10):
#         print("{} x {} = {}".format(i,j,i*j),end="\t")
#     print()

# for i in range(1,10):
#     for j in range(2,10):
#         print("{} x {} = {}".format(j,i,j*i),end="\t")
#     print()

# for i in range(1,10):
#     for j in range(2,10):
#         print("{} X {} = {}".format(j,i,i*j),end="\t")
#     print()


a = 1
for i in range(0,5):
    for j in range(0,a):
            print("상위 for문 {}일때 하위 for문: {:5}".format(i,a*))


# sum = 0
# for i in range(1,101):
#     sum += i
# print("합: {}".format(sum))

# sum = 0
# sum1 = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         if i % 7 == 0:
#             sum += i
#             sum1 += 1
# print("합: {} 개수: {}".format(sum,sum1))

# for i in range(2,10):
#     for j in range(1,10):
#         if i % 9 == 0:
#             print("{} x {} = {}".format(i,j,i*j))

# s = int(input("시작값: "))
# e = int(input("끝값: "))
# g = int(input("증가값: "))
# for i in range(s,e+1,g):
#     if i % 7 == 0:
#         print("7의 배수: {}".format(i))
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
# for i in range(a,b+1):
#     sum += i
# print("합: {}".format(sum))

# won = 10
# sum = 0
# for i in range(1,31):
#     sum += won
#     won *= 2

# print("총금액: {:,}".format(sum))
# n = int(input("몇각형? "))
# import turtle
# import turtle as t
# for i in range(1,n+1):
#     t.forward(100)
#     t.left(360/n)
#     t.mainloop
# import turtle
# n = int(input("몇각형? "))
# import turtle as t
# for i in range(1,n+1):
#     t.forward(100)
#     t.left(360/n)
#     t.mainloop()

# import turtle

# num1 = int(input("몇각형? "))

# for i in range(1,num1+1):
#     turtle.forward(100)
#     turtle.left(360/num1)

# turtle.mainloop()


# n = int(input("수입력: "))
# if 1 <= n <= 9:
#     for i in range(1,n+1):
#         for j in range(1,10):
#          if i % n == 0:
#             print("{} * {} = {}".format(i,j,i*j))

# n = int(input())
# for i in range(1,10):
#     print(n,"*",i,"=",n*i)

# a = int(input())
# b = int(input())
# for i in range(1,10):

# a = int(input())
# b = int(input())
# if a > b:
#     print("{}".format(">"))
# elif a < b:
#     print("{}".format("<"))
# elif a == b:
#     print("{}".format("=="))