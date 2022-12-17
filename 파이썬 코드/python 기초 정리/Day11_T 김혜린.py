# 문제3

# # 1번(*연산자)
# for i in range(5):
#     print("상위 For문 {}일때 하위 For문".format(i),end=":")
#     for j in range(5):
#         print(i*j,end="")
#     print()

# #2번(+연산자)
# a = b = c = d = e = 0

# for i in range(5):
#     print("상위 For문 {}일때 하위 For문".format(i),end=":")
#     for j in range(1):
#         print("{}{}{}{}{}".format(a,b,c,d,e))
#         b += 1
#         c += 2
#         d += 3
#         e += 4



# # 문제4

# # 1번
# for i in range(5):
#     for j in range(1,6):
#         print(j+5*i,end="\t")
#     print()

# # 2번 -> 다양하게 해보기!
# for i in range(1,22,5):
#     for j in range(5):
#         print(i+j,end="\t")
#     print()

# # 3번
# a = 0
# for i in range(5):
#     for j in range(5):
#         a += 1
#         print(a,end="\t")
#     print()


#예제8

# #for문
# a = 0
# b = 0

# for i in range(1,11):
#     if i % 2 == 0:
#         a += i
#     else:
#         b +=i

# print("짝수 합: {} 홀수 합: {}".format(a,b))

# # while문
# a = 0
# b = 0

# i = 1
# while i < 11:
#     if i % 2 == 0:
#         a += i
#     else:
#         b +=i
    
#     i += 1

# print("짝수 합: {} 홀수 합: {}".format(a,b))


# # 예제9

# i = 0 # 시작값

# while i < 5: # 종료값 

#     print(i)

#     i += 1 # 증가값

# else:
#     print(i)

# #예제10

# while True:
#     print("망함....")


# # 예제11

# a = True

# i = 1

# while a:
#     print(i)

#     if i == 10:
#         a = False

#     i += 1


# # 예제14

# #1번
# while True:
#     m = int(input("월을 입력하세요: "))

#     if 1 <= m <= 3:
#         print("{}월은 봄입니다.".format(m))
         
#     elif 4 <= m <= 6:
#         print("{}월은 여름입니다.".format(m))

#     elif 7 <= m <= 9:
#         print("{}월은 가을입니다.".format(m))
    
#     elif 10 <= m <= 12:
#         print("{}월은 겨울입니다.".format(m))

#     else:
#         print("잘못입력하셨습니다.")
#         continue
#     break
# print("반복종료")


# #2번
# while True:
#     m = int(input("월을 입력하세요: "))
#     if 1 <= m <= 12:
#         if 1 <= m <= 3:
#             print("{}월은 봄입니다.".format(m))
            
#         elif 4 <= m <= 6:
#             print("{}월은 여름입니다.".format(m))

#         elif 7 <= m <= 9:
#             print("{}월은 가을입니다.".format(m))
        
#         elif 10 <= m <= 12:
#             print("{}월은 겨울입니다.".format(m))
#         break

#     else:
#         print("잘못입력하셨습니다.")

# print("반복종료")

# # continue키워드 사용법 예시 ) 3의배수만 출력X
# for i in range(1,101):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i)


# #문제6

# while True:
#     user = int(input("입력: "))

#     if user == 0:
#         print("프로그램 종료!")
#         break

#     else:
#         print("다시 입력해주세요.")

# 문제7 
a = 0
while True:
    user = int(input("입력: "))
    a += user 
    if user == 0:
        print("프로그램 종료!")
        print("합: {}".format(a))
        break

    else:
        print("다시 입력해주세요.")

# # 문제8

# for i in range(5):
#     for j in range(10):
#         print("*",end=" ")
#     print()

# 문제9

# 숙제 정답

# 문제1) 1 ~ 100까지 합을 구하시오

sum1 = 0

for i in range(1,101):
    sum1 += i

print(sum1)

# 문제2) 1~100사이값 중 2의 배수이며 7의 배수에 해당하는 경우 개수와 합을 구하시오.

a = 0
b = 0
for i in range(1,101):
    if i % 2 == 0:
        if i % 7 == 0:
            a += 1
            b += i

            print("개수: {}\t합: {}".format(a,b))


# 문제3) 중첩 for문 사용하여 9단만 출력 해보기

for i in range(9,10):
    for j in range(1,10):
        print("{} X {} = {}".format(i,j,i*j))

