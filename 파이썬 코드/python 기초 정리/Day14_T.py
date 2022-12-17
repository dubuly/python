# # 정리하기 문제1

# rice = 100 * 1000
# mouse = 2
# day = 1

# while True:

#     rice -= mouse*20

#     if day % 10 == 0:
#         mouse *= 2

#     if rice <= 0:
#         break

#     day += 1

# print("{} 일 {} 마리".format(day,mouse))

# # 리스트 선언
# list_1 = [300,30,333,"문자열",True]

# # 실행
# print(list_1)

# # 인덱스

# # 리스트명[인덱스] 

# # 정방향
# print(list_1[0])
# print(list_1[1])
# print(list_1[2])

# # 슬라이싱

# # 리스트명[시작인덱스:끝인덱스]

# # [300,30,333]
# print(list_1[0:3])

# # [300,30,333,"문자열"]
# print(list_1[0:4])

# # [333]
# print(list_1[2:3])

# # 역방향

# # True
# print(list_1[-1])

# # 333
# print(list_1[-3])

# # 300
# print(list_1[-5])


# # 인덱스 사용전

# a = 0 
# b = 0 
# c = 0

# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))

# sum1 = a + b + c

# print(sum1)

# # 인덱스 사용후

# a = [0,0,0]

# a[0] = int(input("수입력: "))
# a[1] = int(input("수입력: "))
# a[2] = int(input("수입력: "))

# sum1 = a[0] + a[1] + a[2]

# print(sum1)

# # 요소 변경

# list_1 = [300,30,333,"문자열",True]

# print(list_1)

# # 300
# list_1[0] = "변경"

# print(list_1)

# # 문제1
# f = ["복숭아","딸기","망고","샤인머스켓","용과","리치","두리안"]
# print(f)

# f[0] = "포도"
# print(f)

# f[-1] = "스테비아토마토"
# print(f)

# f[4:6] = "귤","수박"
# print(f)



# # 문자열 -> 인덱스 사용 O

# a = "포메라니안"

# print(a[0]) 

# print(a[1]) 

# print(a[2]) 

# print(a[3])

# print(a[4]) 


# # 문제2

# a = input("수 입력: ")

# b = a[-1]

# # print(b)

# if b == "0" or b == "2" or b == "4" or b == "6" or b == "8":
#     print("{}은 짝수 입니다.".format(a))

# else:
#     print("{}은 홀수 입니다.".format(a))



# # 멤버 연산자

# # True
# print(1 in (1,2,3))
# print(1 not in (2,3))

# # False
# print(1 in (2,3))
# print(1 not in (1,2,3))


# 문제3
#1번
# a = input("수 입력: ")

# b = a[-1]

# # print(b)

# if b in ("0","2","4","6","8"):
#     print("{}은 짝수 입니다.".format(a))

# else:
#     print("{}은 홀수 입니다.".format(a))


# #2번
# a = input("수 입력: ")

# b = a[-1]

# # print(b)

# if b in "02468":
#     print("{}은 짝수 입니다.".format(a))

# else:
#     print("{}은 홀수 입니다.".format(a))



# # 리스트에 이중으로 접근

# list_1 = [300,30,333,"문자열",True]

# # 문자열
# print(list_1[3])

# # 문
# print(list_1[3][0])

# # 자
# print(list_1[3][1])

# # 열
# print(list_1[3][2])

# # 333
# print(list_1[2])

# # # 3 -> 에러
# # print(list_1[2][0])


# # 리스트안에 리스트 사용

# list_2 = [[1,2,3],["넷","다섯","여섯"],[7,8,9]]

# # ["넷","다섯","여섯"]
# print(list_2[1])

# # 다섯
# print(list_2[1][1])

# # 섯
# print(list_2[1][1][1])

# #[7,8,9]
# print(list_2[2])
# # 9
# print(list_2[2][2])


# # IndexError 

# list_3 = ["가을","9월26일","11시21분"]

# print(list_3[2])

# # print(list_3[3])

# # IndexError: list index out of range


# # 문제4

# A = ["red","green","yellow","apple","is","delicious"]

# print(A[0:3])

# print(A[0],A[3],A[4],A[5])

# # 문제5

# A = [["a","p","p","l","e"],
#     ["python","is","funny"],
#     ["happy","new","year","HI","BYE"]]

# B = ["apple"]

# 반복문 + len함수 사용

# A -> for문
# for i in range(len(A)): # 3
#     for j in range(len(A[i])): # 5,3,5
#         print(A[i][j],end=" ")
#     print()

# B -> for문
# for i in range(len(B[0])):
#     print(B[0][i],end=" ")
# print()

# B -> 중첩 for문
# for i in range(len(B)): # 1
#     for j in range(len(B[0])): # 5
#         print(B[i][j],end=" ")
#     print()



# print(A[0][0],A[0][1],A[0][2],A[0][3],A[0][4])
# print(A[1][0],A[1][1],A[1][2])
# print(A[2][0],A[2][1],A[2][2])

# print(B[0][0],B[0][1],B[0][2],B[0][3],B[0][4])


# # len() 

# # 문자열 길이

# a = "포메라니안"

# print(len(a))

# # 리스트의 요소의 개수

# b = [1,2,3,4,5,6,7]

# print(len(b))

a = input("수입력: ")
b = a[-1]
if b in "02468":
    print("{}는 짝수".format(a))
else:
    print("{}는 홀수".format(a))