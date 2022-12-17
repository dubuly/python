# # 정리하기 문제1

# a = [10,20,30,40,50,60,70]

# # 1번
# print(sum(a))

# # 2번
# sum1 = 0
# for i in a:
#     sum1 += i
# print(sum1)

# # 3번
# sum2 = 0
# for i in range(len(a)):
#     sum2 += a[i]
# print(sum2)

# # 정리하기 문제2

# from random import randrange

# a = []
# b = 0

# while True:
#     rand = randrange(1,46)
#     print(rand)

#     if rand not in a:
#         a.append(rand)
#         b += 1
#         if b == 6:
#             break

# print()
# print(a)


# # 정리하기 문제3

c = [["펭수","펭귄",20],["범이","물개",21],["번개맨","사람",30]]

# # for문 1번

# for i in c:
#     print("이름: {}".format(i[0]))
#     print("특징: {}".format(i[1]))
#     print("나이: {}".format(i[2]))
#     print()


# # for문 2번

for i in range(len(c)):
    for j in range(len(c[i])):
        if j == 0:
            print("이름: {}".format(c[i][j]))
        elif j ==1:
            print("특징: {}".format(c[i][j]))
        else:
            print("나이: {}".format(c[i][j]))
    print()

# # 정리하기 문제4

# 결과값 저장
구구단 = []

for i in range(2,10):
    구구단.append([])
    for j in range(1,10):
        구구단[i-2].append(i*j)

# print(구구단)

# 출력
for i in range(2,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,구구단[i-2][j-1]),end="\t")
    print()


# # 정리하기 문제5

# # 메뉴 등록/ 메뉴별 가격 확인 / 메뉴 가격 수정 / 종료
# m = {}

# while True:
#     print("----- MENU -----")
#     print("1. 메뉴 등록")
#     print("2. 메뉴별 가격 확인")
#     print("3. 메뉴 가격 수정")
#     print("4. 종료")
#     print("-----------------")
#     menu = int(input("선택: "))
#     print()
#     if menu == 1:
#         name = input("메뉴 이름: ")
#         if m.get(name) == None:
#             m[name] = int(input("가격: "))
#         else:
#             print("입력하신 메뉴는 이미 존재합니다.")

#     elif menu == 2:
#         for k,v in m.items():
#             print("메뉴: {}       가격: {}".format(k,v)) 

#     elif menu == 3:
#         name = input("메뉴 이름: ")
#         if m.get(name) == None:
#             print("입력하신 메뉴는 존재하지 않습니다.")
#         else:
#             m[name] = int(input("가격: "))

#     elif menu == 4:
#         print("종료")
#         break
#     else:
#         print("잘못입력하셨습니다.")


# String

# # 예제1)

# st = "Python String"

# # find()
# print(st.find("String"))
# print(st.find("String",1))

# # count()
# print("Python String".count("t"))

# # lower() - 소문자
# print(st.lower())

# # upper() - 대문자
# print(st.upper())

# # 예제2)

# st2 = "   Python String   "

# print(st2)

# # strip()

# print(st2.strip())

# # rstrip() - 오른쪽공백
# print(st2.rstrip())

# # lstrip() - 왼쪽공백
# print(st2.lstrip())

# #예제3) 

# st3 = "Python String"

# print(st3)

# # replace()
# print(st3.replace("String","문자열"))

# # split()
# print(st3.split())
# print(st3.split("t"))


# #문제1

# st = "It is a fun python class"

# print(len(st))
# print(st.count("a"))
# print(st.count("s"))

# # 문제2 (함수 없이 풀어보기!)
# st3 = "Have a nice day"

# print(st3.count("a"))
# print(st3.count("day"))
# print(st3.count("dak"))

# 문제3
st = """김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월 14일
어피치 -2022년 11월 20일
라이언 - 2030년 1월 10일"""

# #1번
# st = st.replace("-",":")
# st = st.replace("2017","1999")
# st = st.replace("2015","1999")
# st = st.replace("2018","1999")

# print(st)

# #2번 (:기준으로)
# st = st.replace("-",":")

# a = 0

# for i in range(3):
#     a = st.find(":",a+1)
#     print(a)
#     st = st.replace(st[a+1:a+5],"1999")

# print(st)


# #3번 (년 기준으로)
# st = st.replace("-",":")

# a = 0

# for i in range(st.count("년")):
#     a = st.find("년",a+1)
#     print(a)
#     st = st.replace(st[a-4:a],"1999")

# print(st)

# 문제4

user = input("이름과 나이 입력(공백구분!): ")

a = user.split(" ")
print(a)

print("이름: {} 나이: {}".format(a[0],a[1]))























