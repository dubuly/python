m = {}

while True:
    print("----- MENU -----")
    print("1. 메뉴 등록")
    print("2. 메뉴별 가격 확인")
    print("3. 메뉴 가격 수정")
    print("4. 종료")
    print("----------------")

    menu = int(input("선택: "))
    print()

    if menu == 1:
        name = input("메뉴 이름: ")
        if m.get(name) == None:
            m[name] = int(input("가격: "))
        else:
            print("입력하신 메뉴는 이미 존재합니다")

    elif menu == 2:
        for k,v in m.items():
            print("메뉴: {}\t가격: {}".format(k,v))

    elif menu == 3:
        name = input("메뉴 이름: ")
        if m.get(name) == None:
            print("입력하신 메뉴는 존재하지 않습니다")
        else:
            m[name] = int(input("가격: "))
        
    elif menu == 4:
        print("종료")
        break
    else:
        print("잘못 입력하셨습니다.")