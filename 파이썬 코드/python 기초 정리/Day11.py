# 중첩 for문 퀴즈 3 정답
# 1번 * 연산 사용
# for i in range(5):
#     print("상위 for문 {}일때 하위 for문".format(i),end=":")
#     for j in range(5):
#         print(i*j,end="")
#     print()

# 2번 + 연산 사용
# a = b= c= d= e = 0
# for i in range(5):
#     print("상위 for문 {}일때 하위 for문".format(i),end=":")
#     for j in range(1):
#         print("{}{}{}{}{}".format(a,b,c,d,e))
#         b += 1
#         c += 2
#         d += 3
#         e += 4

# 문제 4
# 방법 1
# for i in range(5):
#     for j in range(1,6):
#         print(j+5*i,end="\t")
#     print()

# 방법 2
# for i in range(1,22,5):
#     for j in range(5):
#         print(i+j,end="\t")
#     print()

# 방법 3
# a = 0
# for i in range(5):
#     for i in range(5):
#         a += 1
#         print(a,end="\t")
#     print()

# 반복문
# while 반복문
# 주어진 조건 식에 따라 반복하여 코드를 실행, while문과 for문은 서로 대체 가능
# while 조건식:
#      수행코드
#      수행코드

# 예제 8
# for문 사용
# sum = 0
# sum1 = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         sum += i
#     elif i % 2 == 1:
#         sum1 += i
# print("짝수합: {} 홀수합: {}".format(sum,sum1))

# while 사용(범위를 지정해주어야 함 아니면 무한 반복)
# sum = 0
# sum1 = 0

# i = 1
# while i < 11:
#     if i % 2 == 0:
#         sum += i
#     elif i % 2 == 1:
#         sum1 += i
#     i += 1

# print("짝수합: {} 홀수합: {}".format(sum,sum1))

# 예제9
# i = 0 # 시작값
# while i < 6: # 종료값
#     print(i)
#     i += 1 # 증가값

# else:
#     print(i)

#  while 반복문 무한 반복
# while True:
#     수행코드
#     수행코드

# 예제 10
# while문 이용하여 무한 반복
# while True:
#     print("망함....")

# 예제 11
# a = True
# i = 1
# while a:
#     print(i)

#     if i == 10:
#         a = False
    
#     i += 1

# break 키워드: 반복의 종료
# while True:
#     수행코드
#     break
#     수행코드

# 예제 12
# while True:
#     print("망함.....")
#     break
#     print("2번째 출력은 나오나요?")
# print("휴.....")

# continue 키워드: 반복의 처음으로 이동
# while True:
#     수행코드
#     continue
#     수행코드

# # 예제 13
# while True:
#     i=int(input("10보다 작은 정수 입력: "))
#     if i < 10:
#         print("10보다 작습니다.")
#         break
#     else:
#         print("말 좀 들어요....")
#         continue
# print("반복 종료!")

# 예제 14
# while True:
#     i = int(input("월? "))
#     if 1 <= i <= 3:
#         print("봄입니다.")
#         break
#     elif 4 <= i <= 6:
#         print("여름입니다.")
#         break
#     elif 7 <= i <= 9:
#         print("가을입니다.")
#         break
#     elif 10 <= i <= 12:
#         print("겨울입니다.")
#         break
#     else:
#         print("잘못입력하셨습니다")
#         continue
# print("반복종료")

# 1번
# while True:
#     i = int(input("월? "))
#     if 1 <= i <= 3:
#         print("봄입니다.")
       
#     elif 4 <= i <= 6:
#         print("여름입니다.")
       
#     elif 7 <= i <= 9:
#         print("가을입니다.")
      
#     elif 10 <= i <= 12:
#         print("겨울입니다.")
#         break
#     else:
#         print("잘못입력하셨습니다")
#         continue
#     break # 맨 마지막에 키워드 넣기
# print("반복종료")

# 2번(continue 키워드 굳이 쓸 필요 x)
# while True:
#     i = int(input("월? "))
#     if 1 <= i <= 12:
#         if 1 <= i <= 3:
#             print("봄입니다.")
       
#         elif 4 <= i <= 6:
#             print("여름입니다.")
       
#         elif 7 <= i <= 9:
#             print("가을입니다.")
      
#         elif 10 <= i <= 12:
#             print("겨울입니다.")
#         break
#     else:
#         print("잘못입력하셨습니다")
       
# print("반복종료")


# continue 키워드 필요한 경우: 어떤 값을 건너뛸 때
# for i in range(1, 101):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i)

# 퀴즈 5
# for i in range(1,6):
#     print(i)
# while True:
#     i < 6
#     print(i)

# 횟수를 중요시하는 반복문은 for문으로 사용, 특정 조건을 중요시 하는 반복문은 while을 사용

# 퀴즈 6
# while True:
#     a = int(input("키 입력: "))
#     if a == 0:
#         break
#     else:
#         print("다시 입력하세요")
# 
# 문제 7
# sum = 0
# while True:
#     a = int(input("수입력: "))
#     sum += a
#     if a == 0:
#         print("프로그램 종료")
#         print("합: {}".format(sum))
#         break
#     else:
#         print("다시 입력하세요")

# 문제 8
# for i in range(5):
#     for j in range(10):
#             print("*",end=" ")
#     print()
        


# for i in range(5):
#         for j in range(1,5):
#                 print(j+5*i,end="\t")
#         print()


# sum = 0
# sum1 = 0
# for i in range(1,11):
#         if i % 2 == 0:
#                 sum += i
#         if i % 2 == 1:
#                 sum1 += i
# print("짝수합: {} 홀수합: {}".format(sum,sum1))



# a = 0
# b = 0

# i = 1
# while i < 11:
#         if i % 2 == 0:
#                 a += i
#         if i % 2 == 1:
#                 b += i

#         i += 1
# print("짝수합: {} 홀수합: {}".format(a,b))


# i = 0
# while i < 6:
#         print(i)
#         i += 1
# # else:
# #         print(i)

# i = 1
# a = True
# while a:
#         print(i)
#         if i == 10:
#                 a = False
#         i += 1
        
# a = True

# i = 1

# while a:
#     print(i)

#     if i == 10:
#         a = False

#     i += 1
# 
# while True:
#         w = int(input("몇월? "))
#         if 1 <= w <= 3:
#                 print("봄입니다")
#         elif 4 <= w <= 6:
#                 print("여름입니다")
#         elif 7 <= w <= 9:
#                 print("가을입니다")
#         elif 10 <= w <= 12:
#                 print("겨울입니다")
#         else:
#                 print("잘못입력하셨습니다")
#                 continue
#         break
# print("반복종료")

# for i in range(1,6):
#         print(i)

# i = 1
# while i < 5:
#         print(i)
#         i += 1
# else:
#         print(i)

# i = 0 # 시작값

# while i < 5: # 종료값 

#     print(i)

#     i += 1 # 증가값

# else:
#     print(i)

# a = int(input("키 입력: "))
# while True:
#         if a == 0:
#                 print("프로그램 종료")
#                 break
#         else:
#                 print("다시입력하세요")

while True:
    user = int(input("입력: "))

    if user == 0:
        print("프로그램 종료!")
        break

    else:
        print("다시 입력해주세요.")
