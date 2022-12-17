# 리스트 연산자

# list_a = ["A","B","C"]
# list_b = ["D","E","F","G","H"]

# # 연결 + 
# print(list_a + list_b)

# # 반복 *
# print(list_a*3)

# # 요소 개수 len()
# print(len(list_a))
# print(len(list_b))

# 문제 6
# sum -> 요소들의 합을 구하는 함수

# a = [1,2,3,4]
# sum = a[0]+a[1]+a[2]+a[3]
# avg = sum/len(a)
# print("평균: {}".format(avg))

# print(sum(a))
# print(len(a))
# print(sum(a)/len(a))

# 리스트 함수
# 함수                                  설명
# append(value)                 리스트 끝에 값을 추가
# insert(idx,value)             특정 인덱스 위치에 값을 추가
# extend()                      리스트 끝에 여러 요소 추가(여러값일때 [] 사용 해야함)
# del()                         특정 요소 삭제
# pop()                         마지막 인덱스 값을 반환후 삭제
# remove(value)                 특정 값에 해당하는 것을 찾아 삭제
# clear()                       모든 값을 삭제하여 빈리스트만 남김


# append(), insert() 사용법

# append(): 맨 뒤
# 리스트명.append(요소)

# insert(): 중간
# 리스트명.insert(위치,요소)

# 리스트 함수

# list_a = ["A","B","C"]

# print("append 사용해서 뒤에 요소 추가")

# # D
# list_a.append("D")

# # E
# list_a.append("E")

# print(list_a)

# print("- insert 중간에 요소 추가")

# # 0번째인덱스에 오늘 날짜 (문자열) 추가
# list_a.insert(0,"9월 27일")

# print(list_a)

# print("- extend 여러 요소 뒤에 추가")

# # "F","G","H" 추가
# list_a.extend(["F","G","H"])

# print(list_a)

# # 리스트 요소 제거
# # 인덱스로 제거 하기: del(), pop()

# # del(): 특정 요소
# # del 리스트명[인덱스]

# # pop(): 특정 요소 & 미입력시 맨 뒤 요소
# # 리스트명.pop(인덱스)

# print("- del 리스트의 특정 요소 하나 제거")

# # 위에서 추가한 오늘 날짜 (문자열) 제거
# del list_a[0]
# print(list_a)

# # A/ () 안에 요소 미입력시 마지막 요소 제거

# print("- pop 리스트의 특정 요소 하나 제거")
# list_a.pop(0)
# print(list_a)

# print("-del 리스트의 특정 요소 여러개 제거")

# del list_a[1:3]
# print(list_a)

# 값으로 제거 하기: remove()
# 리스트.remove(값)

# list_b = [1,2,3,1,2,3,1,2,3]

# print("- remove 값으로 제거")

# 내부에 있는 2 제거
# list_b.remove(2)

# for i in range(3):
#     list_b.remove(2)
# print(list_b)


# 모두 제거: clear
# clear(): 내부의 모든 요소를 제거
# 리스트.clear()

# list_c = [1,2,3,4,5]

# print("- clear 리스트 내부 모든 요소 제거")

# list_c.clear()
# print(list_c)


# 문제 7
# A = [0,1,2,3,4,5,6,7,8,9]

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

# 핵심 포인트
# 리스트: 여러가지 자료를 저장할 수 있는 자료형
# 요소: 리스트 내부에 있는 각각의 자료
# 인덱스: 리스트 내부에서 값의 위치를 표현
# -> for 반복문과 함께 자주 사용된다

# list_1 = [273,32,103,57,52]
# for i in list_1:
#     print(i)

# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     if i >= 100:
#         if i % 2 == 0:
#             print("100 이상의 짝수: {}".format(i))
#         else:
#             print("100 이상의 홀수: {}".format(i))

# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     print("{}의 자리수는 {} 입니다.".format(i,len(str(i))))

# 문제 3
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

# 딕셔너리: 키를 사용하여 여러 자료를 저장하는 자료형

# point) 리스트는 인덱스를 기반으로 값을 저장/ 딕셔너리는 키를 기반으로 값을 저장
# 리스트: 변수 = []
# 딕셔너리: 변수 = {}

# 딕셔너리 사용법
# 변수명 = {키:값}

# dict_a = {"name":"펭수","age":20}
# print(dict_a)

# # 특정 키의 값을 출력하기
# # print(변수명["키값"])

# print(dict_a["name"])
# print(dict_a["age"])

# # 딕셔너리 + 리스트: 하나의 자료로 함께 사용 가능
# # 딕셔너리 사용
# dict_a = {"name":"펭수","age":20}

# # 딕셔너리 + 리스트 사용
# dict_b = {"workmate":["뚝딱이","범이","뿡뿡이","번개맨","EBS 사장님"]}
# print(dict_b)

# 특정 키의 값 출력하기
# 자료형            선언 형식                   사용 방법
# 리스트            list_a=[]                    list_a[1]
# 딕셔너리          list_b={}                   dict_a["name"]



# 특정 키의 값 제거하기
# del 변수명["키값"]


# 예제 1

# 1. 선언
dict_c = {
    "name":"펭수",
    "age":20,
    "workmate":["뚝딱이","범이","뿡뿡이","번개맨","EBS 사장님"],
    "birthplace":"남극"
}

# 2. 특정 키의 값 출력
# print(dict_c["name"])
# print(dict_c["age"])
# print(dict_c["workmate"])
# print(dict_c["birthplace"])

# 3. 리스트 값 출력
# 뿡뿡이
# print(dict_c["workmate"][2])

# 4. 키 - 값 추가
dict_c["food"]="파스타"
print(dict_c)

# 5. 기존의 값을 새로운 값으로 대치
dict_c["food"]="동원참치"
print(dict_c)

# 6. 특정 키의 값 제거하기
del dict_c["food"]
print(dict_c)