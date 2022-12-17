# # 서식 문자

# #1. 단일 문자

# #C 스타일
# print("%c%c" %("안","녕"))

# # 안
# print("%c" %("안"))
# # 녕
# print("%c" %("녕"))

# #P 스타일
# print("{}{}" .format("안","녕"))

# # 안
# print("{}" .format("안"))
# # 녕
# print("{}" .format("녕"))

# #2. 문자열 및 정수 출력

# #C 스타일
# print("%s님의 나이는 %d세 입니다." %("펭수",20))

# #P 스타일
# print("{}님의 나이는 {}세 입니다." .format("펭수",20))

# #3. 문자열 및 실수 출력

# #C 스타일
# print("%s님의 키는 %fcm 입니다." %("펭수",12.345))
# print("%s님의 키는 %.2fcm 입니다." %("펭수",12.345))

# #P 스타일
# print("{}님의 키는 {:f}cm 입니다." .format("펭수",12.345))
# print("{}님의 키는 {:.2f}cm 입니다." .format("펭수",12.345))


# #4. 고정길이 출력

# #C 스타일
# print("%d원\n%10d원" %(10000,200000))

# #P 스타일
# print("{}원\n{:10}원" .format(10000,200000))



# #5. 정렬하여 출력

# #C 스타일
# print("%10s" %("오른쪽 정렬"))
# print("%-10s" %("왼쪽 정렬"))
# print("%10s,%-10s" %("오른쪽 정렬","왼쪽 정렬"))

# #P 스타일
# print("{:>10}" .format("오른쪽 정렬"))
# print("{:<10}" .format("왼쪽 정렬"))
# print("{:>10},{:<10}" .format("오른쪽 정렬","왼쪽 정렬"))



# # 6. 빈 여백 0으로 채운 후 출력

# #C 스타일
# print("%5d %05d" %(1,1))

# #P 스타일
# print("{:5} {:05}" .format(1,1))

# # 7.추가

# #P 스타일
# print("{:>5},{:하>20,}".format(1,1000000000))
# print("{:>5},{:*>20}".format(1,1000000000))
# print("{:>5},{:_>20}".format(1,1000000000))

# print("{:,}원" .format(1000000000))


# # 문제
# print("\t\t{}".format("파이썬 쇼핑몰"))
# print("번호 : {}" .format("1078718855"))
# print("주소 : {}" .format("서울시 종로구 종로3가"))
# print("{} : {}" .format("성명","김사장"))
# print("{} : {}".format("전화","070-1234-5678"))
# print("{}".format("-"*46))
# print("\t{}\t\t{}\t{}\t{}".format("품명","단가","수량","금액"))
# print("{}".format("-"*46))
# print("{:>10}\t{:,}\t{:>4}\t{:,}".format("블루투스 이어폰",85000,1,85000))
# print("{:>14}\t{:>14,}\t{:>4}\t{:>6,}".format("USB3.0 8G",8000,1,8000))
# print("{}".format("-"*46))
# print("{}\t\t\t\t\t{:>6,}".format("소 계",93000))
# print("{}".format("-"*46))
# print("{}\t\t\t\t{:,}".format("청구금액",93000))
# print("{}\t\t\t{:>14,}".format("받은금액",100000))
# print("{}\t\t\t\t{:>6,}".format("거스름돈",7000))
# print("{}".format("-"*46))


# # 변수

# # 1. 선언 (a,b,c)

# # 2. 할당 (a -> int값 , b -> float값 c -> str값)

# # 3. 참조 (print()사용)

# a = 907

# print(a)

# b = 9.07

# print(b)

# c = "오늘은 9월7일 입니다."

# print(c)


# # type을 확인 -> type()

# print(type(a))
# print(type(b))
# print(type(c))


# # 키워드 확인

# import keyword
# False = 10 # SyntaxError: cannot assign to False -> 구문 에러 발생
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as',
# 'assert', 'async', 'await', 'break','class',
# 'continue', 'def', 'del', 'elif','else', 
# 'except', 'finally', 'for', 'from','global',
# 'if', 'import', 'in', 'is', 'lambda', 
# 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']


# # 함수명을 변수명으로 사용X
# print = 10
# print(1)




# # 판별법

# a
# b
# c
# False
# print


# # 변수 선언시 변수명만 보고도 어떤 자료를 가지고 있는지 유추 가능하게 설정

# # 나쁜 예
# a = "펭수"

# # 좋은 예
# name = "펭수"