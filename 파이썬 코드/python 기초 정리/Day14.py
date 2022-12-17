# 정리하기 문제 1

# rice = 100 * 1000
# mouse = 2
# day = 1

# while True:
#     rice -= mouse * 20

#     if day % 10 == 0:
#         mouse *= 2

#     if rice <= 0:
#         break

#     day += 1

# print("{}일 {}마리".format(day,mouse))

# 자료형
# 리스트(list): 리스트는 여러가지 자료를 저장할 수 있는 자료형
# 변수명 = [요소(element)]

# 리스트 선언
# list_1 = [300,30,333,"문자열",True]

# 실행
# print(list_1)

# 인덱스: 리스트의 특정 값에 접근하기 위한 방법
# print(변수명[시작범위:끝범위-1])
# list_1 = [300,30,333,"문자열",True]
# 인덱스    [0] [1] [2]   [3]    [4]

# 인덱스 역방향
# list_1 = [300,30,333,"문자열",True]
# 인덱스    [-5][-4][-3]  [-2]   [-1]


# 정방향
# print(list_1[0])
# print(list_1[1])
# print(list_1[2])

# 슬라이싱(끝범위 -1 처리)

# 리스트명[시작인덱스:끝인덱스]

# 300,30,333
# print(list_1[0:3])

# [300,30,333,"문자열"]
# print(list_1[0:4])

# [333]
# print(list_1[2:3])

# 역방향
# True
# print(list_1[-1])

# print(list_1[-3])

# print(list_1[-5])



# 인덱스 사용전

# a = 0
# b = 0
# c = 0
# a = int(input("수입력: "))
# b = int(input("수입력: "))
# c = int(input("수입력: "))
# total = a + b + c
# print(total)

# 인덱스 사용후

# a = [0,0,0]

# a[0] = int(input("수입력: "))
# a[1] = int(input("수입력: "))
# a[2] = int(input("수입력: "))

# total = a[0] + a[1] + a[2]

# print(total)

# 요소 변경
# list_1 = [300,30,333,"문자열",True]
# print(list_1)

# # 300
# list_1[0] = "변경"

# print(list_1)

# 문제 1
# list = ["딸기","복숭아","망고","포도"]
# list[0] = "자두"
# print(list)

# list = ["딸기","복숭아","망고","포도"]
# list[0:2] = "자두","사과","배","바나나","키위"
# print(list)

# 문자열 -> 인덱스 사용 가능

# a = "포메라니안"

# print(a[0])

# print(a[3])

# print(a[4])

# 문제 2
# a = input("수 입력: ")
# b = a[-1]

# if b == "0" or b == "2" or b == "4" or b == "6" or b == "8":
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 홀수".format(a))

# 멤버 연산자: 산술식을 구성하는 요소
# 연산자       예제                 설명
#  in       1 in [1,2,3]        왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재하면  True
# not in    1 not in [1,2,3]    왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재하지 않으면 True



# 멤버 연산자 사용식

# a = input("수입력: ")
# b = a[-1]

# if b in "02468":
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 짝수".format(a))



# 멤버 연산자
# True
# print(1 in (1,2,3))
# print(1 not in (2,3))

 # False
# print(1 in (2,3))
# print(1 not in (1,2,3))


# 리스트에 이중으로 접근(문자열만 가능)
list_1 = [300,30,333,"문자열",True]

# 문자열
# print(list_1[3])

# # 문
# print(list_1[3][0])

# # 자
# print(list_1[3][1])

# # 열
# print(list_1[3][2])

# 333
# print(list_1[2])

# # 3 -> 에러
# print(list_1[2][0])


# 리스트 안에 리스트 사용
list_2 = [[1,2,3],["넷","다섯","여섯"],[7,8,9]]

# ["넷","다섯","여섯"]
# print(list_2[1])

# # "다섯"
# print(list_2[1][1])

# #  "섯"
# print(list_2[1][1][1])

# # [7,8,9]
# print(list_2[2])

# # 9
# print(list_2[2][2])

# IndexError: list index out of range

# list_3 = ["가을","9월26일","11시21분"]

# print(list_3[2])
# print(list_3[3])

# 문제4
# A = ["red","green","yelllow","apple","is","delicious"]
# print(A[0:3])
# print(A[0],A[3],A[4],A[5])

# 문제 5
A = [["a","p","p","l","e"],["python","is","funny"],["happy","new","year"]]

B = ["apple"]

# print(A[0][0],A[0][1],A[0][2],A[0][3],A[0][4])
# print(A[1][0],A[1][1],A[1][2])
# print(A[2])
# print(B[0])


# len(): 문자열 길이 설정

# a = "포메라니안"

# print(len(a))

# # 리스트의 요소의 개수

# b = [1,2,3,4,5,6,7]

# print(len(b))

# print(len(A))
# print(len(B))

# 반복문 + len 함수 사용
A = [["a","p","p","l","e"],["python","is","funny"],["happy","new","year"]]
print(len(A))

# for i in range(0,2):
#     for j in range(1):
#         print(A,B)