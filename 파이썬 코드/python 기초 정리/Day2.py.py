# a = int(input("선택: "))
# print("1. easy game start")
# print("2. hard game start")
# print("3. exit")
# if a == 1:
#     print("easy game start")
# if a == 2:
#     print("hard game start")
# if a == 3:
#     print("exit")

# a = int(input("수입력: "))
# if a % 2 == 0:
#     print("{}는 짝수 입니다.".format(a))
# else:
#     print("{}는 홀수 입니다.".format(a))

# a = int(input("수입력: "))
# if a % 3 == 0:
#     print("{}는 3의 배수".format(a))
# else:
#     print("{}는 3의 배수가 아니다.".format(a))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# if a > b:
#     print("{}는 {}보다 크다.".format(a,b))
# else:
#     print("{}는 {}보다 크다.".format(b,a))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# if a > b and a > c:
#     print("{}는 제일 큰 수".format(a))
# if b > c and b > a:
#     print("{}는 제일 큰 수".format(b))
# if c > a and c > b:
#     print("{}는 제일 큰 수".format(c))

    
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# if a > b and a > c:
#     print("{}는 제일 큰 수".format(a))
# if b > c and b > a:
#     print("{}는 제일 큰 수".format(b))
# else:
#     print("{}는 제일 큰 수".format(c))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# if a > b and a > c:
#     print("{}는 제일 큰 수".format(a))
# else:
#     if b > c and b > a:
#         print("{}는 제일 큰 수".format(b))
#     else:
#         print("{}는 제일 큰 수".format(c))

# a1 = int(input("수입력: "))
# a2 = int(input("수입력: "))
# a3 = int(input("수입력: "))
# if a1 > a2 and a1 > a3:
#     print("제일 큰 수: {}".format(a1))
# if a2 > a3 and a2 > a1:
#     print("제일 큰 수: {}".format(a2))
# else:
#     print("제일 큰 수: {}".format(a3))


# a1 = int(input("수입력: "))
# a2 = int(input("수입력: "))
# a3 = int(input("수입력: "))
# if a1 > a2 and a1 > a3:
#     print("제일 큰 수: {}".format(a1))
# elif a2 > a1 and a2 > a3:
#     print("제일 큰 수: {}".format(a2))
# elif a3 > a1 and a3 > a2:
#     print("제일 큰 수: {}".format(a3))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# if a > b and a % 2 ==0:
#     print("{}는 큰 수이면서 짝수".format(a))
# if b > a and b % 2 ==0:
#     print("{}는 큰 수이면서 짝수".format(b))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# if a > b:
#     if a % 2 == 0:
#         print("{}는 큰 수이면서 짝수".format(a))
# if b > a:
#     if b % 2 == 0:
#         print("{}는 큰 수이면서 짝수".format(b))

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# total = a + b
# if total % 2 ==0 and total % 3 ==0:
#     print("{}는 짝수이고 3의 배수".format(total))
# else:
#     print("해당사항 없음")

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# if a > b and a > c:
#     print("{}는 가장 큰 수".format(a))
# elif b > a and b > c:
#     print("{}는 가장 큰 수".format(b))
# else:
#     print("{}는 가장 큰 수".format(c))

# a = int(input("1 ~ 4 입력: "))
# if a == 1:
#     print("{}는 1 입니다.".format(a))
# elif a == 2:
#     print("{}는 2 입니다.".format(a))
# elif a == 3:
#     print("{}는 3 입니다.".format(a))
# elif a == 4:
#     print("{}는 4 입니다.".format(a))
# else: 
#     print("잘못입력하셨습니다.")

# elif 가 없을 경우
# a = int(input("1 ~ 4 입력: "))
# if a == 1:
#     print("{}는 1 입니다.".format(a))
# else:
#     if a == 2:
#         print("{}는 2 입니다.".format(a))
#     else:
#         if a == 3:
#             print("{}는 3 입니다.".format(a))
#         else:
#             if a == 4:
#                 print("{}는 4 입니다.".format(a))
#             else:
#                 print("잘못입력하셨습니다.")

# a = int(input("1 ~ 4 입력: "))
# if 1 <= a <= 4:
#     print("{} 입니다.".format(a))
# else:
#     print("잘못입력하셨습니다.")

# a = int(input("1 ~ 4 입력: "))
# if a == 1 or a ==2 or a == 3 or a== 4:
#     print("{} 입니다.".format(a))
# else:
#     print("잘못입력하셨습니다.")

# 3 ~ 5 봄
# 6 ~ 8 여름
# 9~ 11 가을
# 12 ~2 겨울

# w = int(input("월: "))
# if 3 <= w <= 5:
#     print("{}월은 봄 입니다.".format(w))
# elif 6 <= w <= 8:
#     print("{}월은 여름 입니다.".format(w))
# elif 9 <= w <= 11:
#     print("{}월은 가을 입니다.".format(w))
# elif w == 12 or w == 1 or w == 2:
#     print("{}는 겨울 입니다.".format(w))
# else:
#     print("해당 없음")

# w = int(input("월: "))
# if 0 < w <= 2 or w == 12:
#     print("{}는 겨울 입니다.".format(w))
# elif 3 <= w <= 5:
#     print("{}월은 봄 입니다.".format(w))
# elif 6 <= w <= 8:
#      print("{}월은 여름 입니다.".format(w))
# elif 9 <= w <= 11:
#      print("{}월은 가을 입니다.".format(w))
# else:
#     print("해당 없음")

# a = int(input("수입력: "))
# if a % 3 == 0:
#     if a % 2 == 0:
#         print("{}는 3의 배수이며 짝수".format(a))
#     else:
#         print("해당 없음 - 1")
# else:
#     print("해당 없음 - 2")

# 차이점 생각해보기!
#1번
# a = int(input("수입력: "))

# if a == 1:
#     print("1입니다.")

# if a == 1:
#     print("1입니다.")

# # 2번
# a = int(input("수입력: "))

# if a == 1:
#     print("1입니다.")

# elif a == 1:
#     print("1입니다.")


# 생각해보기

num1 = int(input("수입력: "))
num2 = int(input("수입력: "))
num3 = int(input("수입력: "))

if num1 > num2:
    if num1 > num3:
        print("가장 큰 수 : {}".format(num1))

    elif num2 > num1:
        if num2 > num3:
            print("가장 큰 수 : {}".format(num2))

else:
    print("가장 큰 수 : {}".format(num3))

# 1,2,3 순서대로 입력시 3이 출력 안되는 이유는....?