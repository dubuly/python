# # 문제4

# print("1. easy game")
# print("2. hard game")
# print("3. exit")

# su = int(input("선택: "))

# if su == 1:
#     print("easy game start")

# if su == 2:
#     print("hard game start")

# if su == 3:
#     print("exit")

#예제3

# if
# su = int(input("수입력: "))

# if su % 2 == 0:
#     print("{}은 짝수 입니다.".format(su))

# if su % 2 == 1:
#     print("{}은 홀수 입니다.".format(su))

# # if ~ else
# su = int(input("수입력: "))

# if su % 2 == 0:
#     print("{}은 짝수 입니다.".format(su))

# else:
#     print("{}은 홀수 입니다.".format(su))


# # 문제5
# su = int(input("수입력: "))

# if su % 3 == 0:
#     print("{}은 3의 배수 O".format(su))

# else:
#     print("{}은 3의 배수 X".format(su))


# # 문제6
# su1 = int(input("수입력: "))
# su2 = int(input("수입력: "))

# if su1 > su2:
#     print("{}은(는) {}보다 큰 수".format(su1,su2))

# else:
#     print("{}은(는) {}보다 큰 수".format(su2,su1))

# 문제7
# su1 = int(input("수입력: "))
# su2 = int(input("수입력: "))
# su3 = int(input("수입력: "))

# if su1 > su2 and su1 > su3:
#     print("제일 큰 수 : {}".format(su1)) 

# if su2 > su1 and su2 > su3:
#     print("제일 큰 수 : {}".format(su2))

# else:
#     print("제일 큰 수 : {}".format(su3))  

# 3,1,2 입력시 에러

# #해결1
# su1 = int(input("수입력: "))
# su2 = int(input("수입력: "))
# su3 = int(input("수입력: "))

# if su1 > su2 and su1 > su3:
#     print("제일 큰 수 : {}".format(su1)) 

# if su2 > su1 and su2 > su3:
#     print("제일 큰 수 : {}".format(su2))

# if su3 > su1 and su3 > su2:
#     print("제일 큰 수 : {}".format(su3))  


# # 해결2
# su1 = int(input("수입력: "))
# su2 = int(input("수입력: "))
# su3 = int(input("수입력: "))

# if su1 > su2 and su1 > su3:
#     print("제일 큰 수 : {}".format(su1)) 

# else:
#     if su2 > su1 and su2 > su3:
#         print("제일 큰 수 : {}".format(su2))

#     else:
#         print("제일 큰 수 : {}".format(su3))  

# #문제8

# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))

# if num1 > num2 and num1 % 2 == 0:
#     print("{}이 크면서 짝수".format(num1))

# if num2 > num1 and num2 % 2 == 0:
#     print("{}이 크면서 짝수".format(num2))


# # and 없다면 ...?

# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))

# if num1 > num2:
#     if num1 % 2 == 0:
#         print("{}이 크면서 짝수".format(num1))

# if num2 > num1:
#     if num2 % 2 == 0:
#         print("{}이 크면서 짝수".format(num2))

# #문제9

# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))

# sum1 = num1 + num2

# if sum1 % 2 == 0 and sum1 % 3 == 0:
#     print("합 -> {}은 짝수이며 3의 배수".format(sum1))
    
# else:
#     print("해당사항X")


# # 문제7 - 추천!
# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# num3 = int(input("수입력: "))

# if num1 > num2 and num1 > num2:
#     print("{}이 제일 큰 수".format(num1))

# elif num2 > num1 and num2 > num3:
#     print("{}이 제일 큰 수".format(num2))

# else:
#     print("{}이 제일 큰 수".format(num3))

# #예제4
# num1 = int(input("1 ~ 4 입력: "))

# if num1 == 1:
#     print("{} 입니다.".format(num1))

# elif num1 == 2:
#     print("{} 입니다.".format(num1))

# elif num1 == 3:
#     print("{} 입니다.".format(num1))

# elif num1 == 4:
#     print("{} 입니다.".format(num1))

# else:
#     print("잘못입력하셨습니다.")


# elif 없을 경우 (2가지 이상)

# #1번
# num1 = int(input("1 ~ 4 입력: "))

# if num1 == 1:
#     print("{} 입니다.".format(num1))
# else:
#     if num1 == 2:
#         print("{} 입니다.".format(num1))
#     else:
#         if num1 == 3:
#             print("{} 입니다.".format(num1))
#         else:
#             if num1 == 4:
#                 print("{} 입니다.".format(num1))
#             else:
#                 print("잘못입력하셨습니다.")


# # 2번
# num1 = int(input("1 ~ 4 입력: "))

# if num1 == 1 or num1 == 2 or num1 == 3 or num1 == 4:
#     print("{} 입니다.".format(num1))

# else:
#     print("잘못입력하셨습니다.")


# # 3번
# num1 = int(input("1 ~ 4 입력: "))

# if 1 <= num1 <= 4 :
#     print("{} 입니다.".format(num1))

# else:
#     print("잘못입력하셨습니다.")



# 문제10 계절 구하기

# 3 - 5 봄
# 6 - 8 여름
# 9 - 11 가을
# 12 - 2 겨울

# 예외처리X

# m = int(input("월을 입력하세요: "))

# if 3 <= m <= 5:
#     print("{}월은 봄 입니다.".format(m))

# elif 6 <= m <= 8:
#     print("{}월은 여름 입니다.".format(m))

# elif 9 <= m <= 11:
#     print("{}월은 가을 입니다.".format(m))

# else:
#     print("{}월은 겨울 입니다.".format(m))

# # 예외처리 O

# # -1 , 13, 1 입력 시 결과 보기 -> 에러

# m = int(input("월을 입력하세요: "))

# if 3 <= m <= 5:
#     print("{}월은 봄 입니다.".format(m))

# elif 6 <= m <= 8:
#     print("{}월은 여름 입니다.".format(m))

# elif 9 <= m <= 11:
#     print("{}월은 가을 입니다.".format(m))

# elif 12 <= m <= 2:
#     print("{}월은 겨울 입니다.".format(m))

# else:
#     print("잘못입력하셨습니다.")


# # 예외처리 1번 방법

# m = int(input("월을 입력하세요: "))

# if 3 <= m <= 5:
#     print("{}월은 봄 입니다.".format(m))

# elif 6 <= m <= 8:
#     print("{}월은 여름 입니다.".format(m))

# elif 9 <= m <= 11:
#     print("{}월은 가을 입니다.".format(m))

# elif m == 12 or m == 1 or m == 2:
#     print("{}월은 겨울 입니다.".format(m))

# else:
#     print("잘못입력하셨습니다.")


# # 예외처리 2번 방법

# m = int(input("월을 입력하세요: "))

# if m < 0 :
#     print("잘못 입력 하셨습니다.")

# elif 3 <= m <= 5:
#     print("{}월은 봄 입니다.".format(m))

# elif 6 <= m <= 8:
#     print("{}월은 여름 입니다.".format(m))

# elif 9 <= m <= 11:
#     print("{}월은 가을 입니다.".format(m))

# elif 13 <= m: 
#     print("잘못 입력 하셨습니다.")

# else:
#     print("{}월은 겨울 입니다.".format(m))


# #예제5
# a = int(input("수입력: "))

# if a % 2 == 0:
#     if a % 3 == 0:
#         print("3의 배수이며 짝수 : {}".format(a))
#     else:
#         print("해당없음 - 1")
# else:
#     print("해당없음 -2")



# # 차이점 생각해보기!
# #1번
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


# # 생각해보기

# num1 = int(input("수입력: "))
# num2 = int(input("수입력: "))
# num3 = int(input("수입력: "))

# if num1 > num2:
#     if num1 > num3:
#         print("가장 큰 수 : {}".format(num1))

# elif num2 > num1:
#     if num2 > num3:
#         print("가장 큰 수 : {}".format(num2))

# else:
#     print("가장 큰 수 : {}".format(num3))

# # 1,2,3 순서대로 입력시 3이 출력 안되는 이유는....?
