# 숙제
# avr = [[90,80,70],[91,81,71],[92,82,72],[93,83,73],[94,84,74],[95,85,75],[96,86,76],[97,87,77],[98,88,78],[99,89,79]]

# # 평균 점수
# for i in range(len(avr)):
#     print("{}번 {}점".format(i+1,sum(avr[i])/len(avr[i])))



# # 총합
# a = 0
# for i in range(len(avr)):
#     a += sum(avr[i]/len(avr[i]))
# print("10명 평균 점수의 총 합: {}점".format(a))


# 활용1

# 빈 딕셔너리에 요소 추가

# dict_d = {}

# print("요소 추가 전 출력 {}".format(dict_d))

# # 자신의 이름, 키, 몸무게 정보 추가

# dict_d["이름"] = "이지수"
# dict_d["키"] = 168
# dict_d["몸무게"] = 54

# print("요소 추가 후 출력 {}".format(dict_d))

# 활용2

# 요소 제거

# dict_e = {
#     "이름":"라이언",
#     "본적":"나주라씨",
#     "반려묘":"춘식이"
# }

# print("요소 제거 이전 출력: {}".format(dict_e))

# # 본적, 반려묘 제거
# del dict_e["본적"]
# del dict_e["반려묘"]

# print("요소 제거 이후 출력: {}".format(dict_e))


# # 활용3

# # 존재하지 않는 키값 출력 -> keyError '본적'

# print(dict_e["본적"])


# 딕셔너리 함수

# 함수                      설명
# update()          사전형 자료에 값을 추가
# get()             사전형의 값을 반환
# keys()            사전 형의 모든 키를 반환
# items()           사전형의 모든 키,값의 쌍을 튜플로 반환
# clear()           모든 키,값을 삭제하여 빈 사전형 자료만 남김

# 반환 기능이 없는 함수는 함수 적용 후 따로 print 해줘야 한다



# 딕셔너리 함수

# print("update() - 사전형 자료에 값을 추가")
# dict_f = {1:"a",2:"b",3:"c"}

# # 4:"d" 추가
# dict_f.update({4:"d"})

# print(dict_f)

# print("get() - 사전형의 값을 반환")

# print(dict_f.get(1))

# print(dict_f.get(2))

# print(dict_f.get(3))

# print(dict_f.get(9)) # -> 존재하지 않는 값을 넣을땐 none 키워드가 보여짐

# print("keys() - 사전형의 모든 키를 반환")

# print(dict_f.keys())

# for i in dict_f.keys():
#     print(i)

# print("values() - 사전형의 모든 값을 반환")

# print(dict_f.values())

# for i in dict_f.values():
#     print(i)

# dict_g = {1:'a',2:'b',3:'c'}

# print("items - 사전형의 모든 키 - 값 쌍을 튜플로 반환")

# print(dict_g.items())

# for k,v in dict_g.items():
#     print(k,"\t",v)

# print("clear() -   모든 키 - 값을 삭제하여 빈 사전형 자료만 남김")

# dict_g.clear()

# print(dict_g)

# a = {1:"A",2:"B",3:"C"}

# a.update({4:"D",5:"F"})
# print(a)

# print(a.get(1))
# print(a.get(2))
# print(a.get(3))
# print(a.items())

# a.clear()
# print(a)

# print(a.keys())
# print(a.values())


# 문제 1

# dict_a = {}

# for i in range(5):
#     k = input("이름(key) 입력: ")
#     v = input("특징(value 입력: ")

#     dict_a.update({k:v})
# print(dict_a)


# 문제 2

# 재고 = {"커피":7,"펜":3,"종이컵":9,"콜라":20,"사이다":9}

# # 1번
# k = input("물건 입력: ")

# print("{}의 수량은 {}개 입니다".format(k,재고[k]))

# 2번
# k = input("물건 입력: ")

# print("{}의 수량은 {}개 입니다".format(k,재고.get(k)))



# 문제 3

재고 = {"커피":7,"펜":3,"종이컵":9,"콜라":20,"사이다":9}

# k = input("물건을 입력하세요: ")

# if k not in 재고:
#     k = input("물건 입력: ")
#     v = input("수량 입력: ")
#     재고.update({k:v})

# print(재고)


# k = input("물건을 입력하세요: ")

# if 재고.get(k) == None:
#     v = int(input("수량 입력: "))
#     재고.update({k:v})
#     print(재고)
# else:
#     print("{}의 수량은 {}개 입니다".format(k,재고.get(k)))



# 문제 4

book = {}
n = int(input("등록할 책 개수를 입력하시오: "))

for i in range(1,n+1):
    k = input("등록 번호를 입력해주세요: ")
    book[k] = input("책이름을 적어주세요: ")

print(book)
