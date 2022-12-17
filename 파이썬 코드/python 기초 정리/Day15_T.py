# # 리스트 연산자

# list_a = ["A","B","C"]
# list_b = ["D","E","F","G","H"]

# # 연결 + 
# print(list_a + list_b)

# # 반복 *
# print(list_a*3)

# # 요소 개수 len()
# print(len(list_a))
# print(len(list_b))

# # 문제6
# a = [1,2,3,4]

# # 1번
# A = a[0] + a[1] + a[2] + a[3]

# print(A/4)

# # 2번
# print(sum(a))
# print(len(a))

# print(sum(a)/len(a))


# # 리스트 함수

# list_a = ["A","B","C"]

# print("- append 사용해서 뒤에 요소 추가")

# # D 
# list_a.append("D")
# # E
# list_a.append("E")

# print(list_a)

# print("- insert 중간에 요소 추가")

# # 0번째 인덱스에 오늘날짜(문자열) 추가

# list_a.insert(0,"9월27일")

# print(list_a)


# print("- extend 여러 요소 뒤에 추가")

# # "F","G","H"추가

# list_a.extend(["F","G","H"])

# print(list_a)

# print("- del 리스트의 특정 요소 하나 제거")

# # 위에서 추가한 오늘날짜(문자열) 제거

# del list_a[0]

# print(list_a)

# print("- pop 리스트의 특정 요소 하나 제거")

# # A -> 미입력시 마지막 요소 제거 H

# list_a.pop()

# print(list_a)


# print("-del 리스트의 특정 요소 여러개 제거")

# del list_a[1:3]

# print(list_a)

# list_b = [1,2,3,1,2,3,1,2,3]

# print("- remove 값으로 제거")

# # 내부에 있는 2 제거

# for i in range(3):
#     list_b.remove(2)

# print(list_b)


# list_c = [1,2,3,4,5]

# print("- clear 리스트 내부 모든 요소 제거")

# list_c.clear()

# print(list_c)


# #문제7
# A = [0,1,2,3,4,5,6,7,8,9]
# print(A)

# A.append(10)
# print(A)

# A.insert(3,0)
# print(A)

# A.extend(A)
# print(A)

# del A[0]
# print(A)

# A.pop(2)
# print(A)

# A.remove(0)
# print(A)

# A.clear()
# print(A)


# # 문제1
# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     if i >= 100:
#         if i % 2 == 0:
#             print("100이상의 짝수: {}".format(i))
#         else:
#             print("100이상의 홀수: {}".format(i))


# # 문제2

a = [200,101,5,32,64,9,72,900,99,99999]

for i in a:
    print("{}의 자리수는 {} 입니다.".format(i,len(str(i))))

# # 문제3
# a = [1,2,3,4,5,6,7,8,9,10,11,12]

# b = [[],[],[]]

# for i in a:
#     b[(i+2)%3].append(i)

# print(b)

# # 추가
# a = [1,2,3,4,5,6,7,8,9,10,11,12]

# b = [[],[],[],[]]

# for i in a:
#     b[(i+3)%4].append(i)

# print(b)


# # 딕셔너리

# dict_a = {"name":"펭수","age":20}

# print(dict_a)

# # 특정 키의 값 출력하기

# print(dict_a["name"])

# print(dict_a["age"])


# # 딕셔너리 + 리스트

# dict_b = {"workmate": ["뚝딱이","범이","뿡뿡이","번개맨","EBS사장님"]}

# print(dict_b)



# # 예제1

# # 1. 선언
# dict_c = {
#     "name":"펭수",
#     "age":20,
#     "workmate": ["뚝딱이","범이","뿡뿡이","번개맨","EBS사장님"],
#     "birthplace":"남극"
# }

# # 2. 특정 키의 값 출력
# print(dict_c["name"])
# print(dict_c["age"])
# print(dict_c["workmate"])
# print(dict_c["birthplace"])

# # 3. 리스트 값 출력
# # 범이
# print(dict_c["workmate"][1])

# # 4. 키 - 값 추가

# print(dict_c)

# dict_c["like food"] = "동원참치"

# print(dict_c)

# # 5. 기존의 값을 새로운 값으로 대치

# dict_c["like food"] = "물고기"

# print(dict_c)

# # 6. 특정 키의 값 제거

# del dict_c["like food"]

# print(dict_c)


#숙제 (10명의 평균 점수 데이터) => 평균 점수의 총합

avr = [[90,80,70],[91,81,71],[92,82,72],[93,83,73],[94,84,74],
[95,85,75],[96,86,76],[97,87,77],[98,88,78],[99,89,79]]

#평균 점수 구하기(10명)

#총합(10명의 평균의 총합)
