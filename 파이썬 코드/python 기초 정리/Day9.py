# print("="*40)
# print("1. 아메리카노")
# print("2. 카페라떼")
# print("="*40)
# m = int(input("메뉴 선택: "))
# print("="*40)
# print("ICE")
# print("HOT")
# print("="*40)
# t = int(input("온도 선택: "))
# if m == 1 and t == 1:
#     print("선택하신 음료는 아이스 아메리카노 입니다.")
# elif m == 1 and t == 2:
#     print("선택하신 음료는 따뜻한 아메리카노 입니다.")
# elif m == 2 and t == 1:
#     print("선택하신 음료는 아이스 카페라떼 입니다.")
# else:
#     print("선택하신 음료는 따뜻한 카페라떼 입니다.")

# t = int(input("시간: "))
# m = int(input("분: "))
# t_m = 60*t + m
# t_1 = (t_m + 30) // 60
# t_2 = (t_m + 30) % 60
# print("30분 후 시간: {}시 {}분".format(t_1,t_2))

# t = int(input("시간: "))
# m = int(input("분: "))
# t_m = 60*t + m - 30
# if t_m < 0:
#     t_m = t_m + 1440
# t_1 = t_m // 60
# t_2 = t_m % 60
# print("30분 전 시간: {}시 {}분".format(t_1,t_2))

# for i in range(11):
#     print("안녕")

# for i in range(0,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)
# for i in range

# st = "string"
# for i in st:
#     print(i)

# a = 0
# for i in range(1,11):
#     a = a + i
#     print(a)

# s = int(input("시작값: "))
# e = int(input("끝값: "))
# m = int(input("중간값: "))
# sum = 0
# for i in range(s,e+1,m):
#     sum += i
#     print(sum)

# s = int(input("시작값: "))
# e = int(input("끝값: "))
# g = int(input("증가값: "))

# sum1 = 0

# for i in range(s,e+1,g):
    
#     sum1 += i

# print(sum1)

# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)



# for i in range(1,31):
#     print(i,end="\t")
#     if i % 5== 0:
#         print()

# for i in range(1,31):
#     if i % 5 != 0:
#         print(i,end="\t")
#     else:
#         print(i)

# for i in range(1,31):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i,end="\t")

# for x in range(10,0,-1):
#     print(x)

# for char in "abcde":
#     print(char,end="  ")

# for i in range(1,31):
#     print(i,end="\t")
#     if i % 5 == 0:
#         print()

# for i in range(1,31):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i,end="\t")

# for i in range(1,31):
#     if i % 5 != 0:
#         print(i,end="\t")
#     else:
#         print(i)

# st = 'It is a fun Python class'
# a = 0
# s = 0
# for i in st:
#     if i == "a":
#         a += 1
#     elif i == "s":
#         s += 1
# print("a의 개수: {} s의 개수: {}".format(a,s))

# num = int(input("수입력: "))
# sum = 0
# sum1 = 0
# for i in range(1,num+1):
#     if num % 2 == 0:
#        sum += i

# for i in range(1,num+1):
#     if num % 2 == 1:
#         sum1 += i

# print("짝수의 합: {} 홀수의 합: {}".format(sum,sum1))

# st = "It is a fun Python class"
# a = 0
# s = 0
# for i in st:
#     if i == "a":
#         a += 1
#     elif i == "s":
#         s += 1

# print("a의 개수: {} s의 개수: {}".format(a,s))


# for i in range(1,21):
#     print(i,end=" ")

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# for i in range(100,50,-1):
#     if i % 2 == 1:
#         print(i, end=" ")

# for i in range(1,51):
#     print(i,end="\t")
#     if i % 5 == 0:
#         print()

# for i in range(1,51):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i,end="\t")
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
# b = 0
# st = "Python basic program language"
# for i in st:
#     if i != " ":
#         b = b + 1
# print(b)
# sum = 0
# n = int(input())
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# sum = 0
# sum1 = 0
# a = int(input("수입력: "))
# for i in range(1,a+1):
#     if a % 2 == 0:
#         sum = sum + i
#     elif a % 2 == 1:
#             sum1 = sum1 + i
# print("짝수의 합: {} 홀수의 합: {}".format(sum,sum1))

# sum = 0
# s = int(input("시작값: "))
# e = int(input("끝값: "))
# m = int(input("증가값: "))
# for i in range(s,e,m):
#     sum += i
# print(sum)

# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)

# for i in range(1,31):
#     print(i,end="\t")
#     if i % 5 == 0:
#         print()

# for i in range(1,31):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i,end="\t")
# f = 0
# u = 0
# st = "It is a fun Python class"
# for i in st:
#     if i == "f":
#         f += 1
#     if i == "u":
#         u += 1
# print("a: {} s: {}".format(f,u))


# sum = 0
# n = int(input("수입력: "))
# for i in range(0,n+1):
#     sum += i
# print(sum)
# sum = 0
# n = int(input("n: "))
# for i in range(1,n+1):
#     sum += i
# print(sum)
# sum = 0
# for i in range(100):
#     n = int(input("n: "))
#     sum += n
# print(sum)
# print(sum/5)

n = int(input("n: "))

   