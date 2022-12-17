# # 문제1

# for i in range(1,11):
#     for j in range(1):
#         print("*"*i)

# 문제2
# # 1번
# for i in range(1,11):
#     for j in range(1):
#         print(" "*(10-i)+"*"*i)

# # 2번
# for i in range(1,11):
#     for j in range(10-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print() 

# sep옵션
# y = 2022
# m = 9
# d = 23

# print(y,m,d,sep="/")

# print("{}/{}/{}".format(y,m,d))

# # 3번
# for i in range(1,11):
#     for j in range(1):
#         print(" "*(10-i),"*"*i,sep="")


# # + 
# for i in range(1,11):
#         print(" "*(10-i),"*"*i,sep="")

# # 문제3
# for i in range(1,11):
#     for j in range(1):
#         print(" "*(10-i),"*"*((2*i)-1),sep="")



# # 문제4
# # 1번
# for i in range(1,11):
#     for j in range(1):
#         print("*"*(11-i))

# # 2번
# for i in range(11,0,-1):
#     for j in range(1):
#         print("*"*i)


# # 문제5
# for i in range(1,11):
#     for j in range(1):
#         print(" "*(i-1),"*"*(11-i),sep="")


# # 문제6
# for i in range(1,11):
#     for j in range(1):
#         print(" "*(i-1),"*"*(21-(i*2)),sep="")


# 문제7

# #1번
# for i in range(1,10):
#     for j in range(1):
#         print(" "*(10-i),"*"*((2*i)-1),sep="")
# for i in range(1,11):
#     for j in range(1):
#         print(" "*(i-1),"*"*(21-(i*2)),sep="")

# # 2번
# for i in range(1,20):
#     for j in range(1):
#         if i <= 10:
#             print(" "*(10-i),"*"*((2*i)-1),sep="")
#         else:
#             print(" "*(i-10),"*"*(39-(i*2)),sep="")

# 정리하기 문제2
# 1. 기획 (ppt참조)

# # 2. 구성
# m = 0 
# while True:
#     print("---- Menu ----")
#     print("1.콜라 / 300")
#     print("2.사이다 / 300")
#     print("3. 커피 / 200")
#     print("4. 돈 넣기")
#     print("5. 잔돈 반환")
#     print("6. 종료")
#     print("--------------")
#     print("현재 금액",m)
#     menu = int(input("메뉴 선택: "))
#     print()
#     if menu == 1:
#         pass
#     elif menu == 2:
#         pass
#     elif menu == 3:
#         pass
#     elif menu == 4:
#         pass
#     elif menu == 5:
#         pass
#     elif menu == 6:
#         pass
#     else:
#         print("잘못입력하셨습니다.")


# # 3. 실행
# import time
# import os

m = 0 
while True:

    print("---- Menu ----")
    print("1.콜라 / 300")
    print("2.사이다 / 300")
    print("3. 커피 / 200")
    print("4. 돈 넣기")
    print("5. 잔돈 반환")
    print("6. 종료")
    print("--------------")
    print("현재 금액",m)

    menu = int(input("메뉴 선택: "))
    print()
    # time.sleep(0.3)
    # os.system("cls")

    if menu == 1:
        if m < 300:
            print("금액이 부족합니다.")

        else:
            print("콜라 맛있게 드세요!")
            m -= 300

    elif menu == 2:
        if m < 300:
            print("금액이 부족합니다.")

        else:
            print("사이다 맛있게 드세요!")
            m -= 300

    elif menu == 3:
        if m < 300:
            print("금액이 부족합니다.")

        else:
            print("커피 맛있게 드세요!")
            m -= 200

    elif menu == 4:
        a = int(input("돈을 넣어주세요: "))
        m += a

    elif menu == 5:
        print("{:,}원의 잔액이 반환됩니다.".format(m))
        m = 0

    elif menu == 6:
        print("종료")
        break

    else:
        print("잘못입력하셨습니다.")

