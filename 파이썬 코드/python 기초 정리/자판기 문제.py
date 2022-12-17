# m = 0
# while True:

#     print("---- Meun ----")
#     print("1. 콜라/ 300")
#     print("2. 사이다/ 300")
#     print("3. 커피/ 200")
#     print("4. 돈 넣기")
#     print("5. 잔돈 반환")
#     print("6. 종료")
#     print("--------------")
#     print("현재금액", m)
#     menu = int(input("메뉴 선택 : "))

#     if menu == 1:
#         if m < 300:
#             print("구매 불가")
#         else:
#             print("콜라 맛있게 드세요!")
#             m -= 300

#     elif menu == 2:
#         if m < 300:
#             print("구매 불가")
#         else:
#             print("사이다 맛있게 드세요!")
#             m -= 300

#     elif menu == 3:
#         if m < 200: 
#             print("구매 불가")
#         else:
#             print("커피 맛있게 드세요!")
#             m -= 200

#     elif menu == 4:
#         money = int(input("돈을 넣어주세요: "))
#         m += money

#     elif menu == 5:
#         print("{:,}원의 잔돈이 반환됩니다.")
#         m = 0

#     elif menu == 6:
#         print("종료")
#         break

#     else:
#         print("잘못 입력하셨습니다.")

m = 0
while True:
    print("---- Menu ----")
    print("1. 콜라/ 300")
    print("2. 사이다/ 300")
    print("3. 커피/ 200")
    print("4. 돈 넣기")
    print("5. 잔돈 반환")
    print("6. 종료")
    print("--------------")
    print("현재 금액",m)
    menu = int(input("메뉴 선택: "))

    if menu == 1:
        if m < 300:
            print("금액이 부족합니다")
        else:
            print("콜라 맛있게 드세요!")
            m -= 300
    elif menu == 2:
        if m < 300:
            print("금액이 부족합니다")
        else:
            print("사이다 맛있게 드세요!")
            m -= 300
    elif menu == 3:
        if m < 200:
            print("금액이 부족합니다")
        else:
            print("커피 맛있게 드세요!")
            m -= 200
    elif menu == 4:
        money = int(input("돈을 넣어주세요: "))
        m += money
    elif menu == 5:
        print("{:,}원이 반환됩니다.".format(m))
        m = 0
    elif menu == 6:
        print("종료")
        break
    else:
        print("잘못 입력하셨습니다")



