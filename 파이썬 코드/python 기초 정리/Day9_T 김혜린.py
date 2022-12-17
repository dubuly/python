# # 반복문

# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")
# print("반복문")

# # 문자열 100번 출력
# for i in range(100):
#     print("문자열")

# # 횟수 출력
# for apple in range(100): # 범위: 0 ~ 99 (횟수: 100번)
#     print(apple)


# #예제1

# for i in range(10):
#     print("9월19일")

# for i in range(11):
#     print(i)


# #예제2
# for i in range(10,0,-1):
#     print("9월19일")

# for i in range(10,0,-1):
#     print("9월19일",i)

# #예제3
# for i in range(1,11):
#     print(i,end=" ")

# for i in range(5,11):
#     print(i,end=" ")

# for i in range(5,11):
#     print(i,end="안녕")


# #예제4
# st = "string"

# for i in st:
#     print(i)

# for i in "안녕하세요":
#     print(i)

# # 문제1
# a = 0
# for i in range(1,11):
#     a = a + i
#     print(a)

# # 복합 연산자

# li = 'ab'
# a = 2
# print(a)

# a += 3
# print(a)
# a -= 4
# print(a)
# a *= 2
# print(a)
# a /= 5
# print(a)
# a //= 3
# print(a)
# a **= 4
# print(a)
# li += 'c'
# print(li)
# li *=4
# print(li)


# # 예제5
# s = int(input("시작값: "))
# e = int(input("끝값: "))
# g = int(input("증가값: "))

# sum1 = 0

# for i in range(s,e+1,g):
    
#     sum1 += i

# print(sum1)


# # 문제1
# a = 0

# for i in range(1,11):
#     a += i

# print(a)


# #문제2
# #1번
# for i in range(1,31):
#     print(i,end="\t")
#     if i % 5 == 0:
#         print()

# #2번
# for i in range(1,31):
#     if i % 5 == 0:
#         print(i)
#     else:
#         print(i,end="\t")


# #3번
# for i in range(1,31):
#     if i % 5 != 0:
#         print(i,end="\t")
#     else:
#         print(i)

# # 문제3    
# st = "It is a fun Python class"

# a = 0
# s = 0

# for i in st:

#     if i == "a":
#         a += 1
#     elif i == "s":
#         s += 1

# print("a의 개수: {} s의 개수: {}".format(a,s))

# 문제4 - 숙제

# 과제 정답

# 문제13
t = int(input("시간: "))
m = int(input("분: "))

t_m = t*60 + m

t_3 = (t_m + 30) // 60
m_3 = (t_m + 30) % 60

print("30분 후 : {}시 {}분".format(t_3,m_3))

# 14번 

# => 0 시 20분 => -값이 나온다 => 조건문 사용해서 해결(23시50분)

# 시간은 24시간을 기준으로 한다.

t = int(input("시간을 입력해주세요: "))
m = int(input("분을 입력해주세요: "))

total = t*60 + m - 30

if total < 0:
    total = total + 1440 

r_t = total //60
r_m = total %60

print("30분 전의 시간 {}시 {}분 ".format(r_t,r_m))

# 문제15
print("="*30)
print("1. 아메리카노")
print("2. 카페라떼")
print("="*30)
m = int(input("메뉴 선택: "))
print("="*30)
print("1. ICE")
print("2. HOT")
print("="*30)
s = int(input("온도 선택: "))

if m == 1 and s == 1:
    print("선택하신 음료는 아이스 아메리카노 입니다.")
elif m == 1 and s == 2:
    print("선택하신 음료는 핫 아메리카노 입니다.")
elif m == 2 and s == 1:
    print("선택하신 음료는 아이스 카페라떼 입니다.")
elif m == 2 and s == 2:
    print("선택하신 음료는 핫 카페라떼 입니다.")
else:
    print("잘못 입력하셨습니다. 다시 입력해주세요.")