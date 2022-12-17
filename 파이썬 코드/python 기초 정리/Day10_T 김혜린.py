# # 문제4 - 숙제

# a = int(input("수입력: "))
# b = 0 
# c = 0 
# for i in range(1,a+1):
#     if i % 2 == 0:
#         b += i
#     else:
#         c += i

# print("짝수 합: {} 홀수 합: {}".format(b,c))


# # 문제5

# s = int(input("시작값: "))
# e = int(input("끝값: "))
# g = int(input("증가값: "))

# for i in range(s,e+1,g):
#     if i % 7 == 0:
#         print(i,end="\t")
# print()


# print("안녕하세요")

# # 문제6

# sum1 = 0

# for i in range(1,101):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             sum1 += i

# print("합: {} 횟수: {}".format(sum1,i))


# #문제7

# su1 = int(input("수입력: "))
# su2 = int(input("수입력: "))

# sum1 = 0

# if su1 < su2:
#     for i in range(su1,su2+1):
#         sum1 += i

#     print("합: {}".format(sum1))

# elif su1 > su2:
#     for i in range(su2,su1+1):
#         sum1 += i

#     print("합: {}".format(sum1))

# else:
#     print("합: 0")


# # 문제8 

# # 오답
# 10737418240
# won = 10

# for i in range(1,31):

#     won *= 2

# print("예금액: {:,}원".format(won))


# # 정답
# 10737418230


# won = 10

# sum1 = 0

# for i in range(1,31):

#     sum1 += won

#     won *= 2

#     print("예금액: {:,}원".format(sum1))


# # 문제9

# import turtle

# num1 = int(input("몇각형? "))

# for i in range(1,num1+1):
#     turtle.forward(100)
#     turtle.left(360/num1)

# turtle.mainloop()


# #예제6
# for i in range(3):
#     print("첫번째 For문")
#     for i in range(2):
#         print("두번째 for문")


# # 예제7
# for i in range(3):
#     for j in range(3):
#         print("이중 For문 (i: {}\tj: {})".format(i,j))


# # 문제1
# for i in range(2,10):
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j),end="\t")
#     print()

# # 문제2
# for i in range(1,10):
#     for j in range(2,10):
#         print("{} X {} = {}".format(j,i,i*j),end="\t")
#     print()

# 문제3 - HW(못푼사람만!!!)

# 문제1) 1 ~ 100까지 합을 구하시오.

# 문제2) 1~100사이값 중 2의 배수이며 7의 배수에 해당하는 경우 개수와 합을 구하시오.

# 문제3) 중첩 for문 사용하여 9단만 출력 하시오.









