# list_1 = [300,30,333,"문자열",True]
# print(list_1[1:3])
# print(list_1[-4])

# a = 0
# b = 0
# c = 0

# a = input("수입력: ")
# b = input("수입력: ")
# c = input("수입력: ")
# total = a + b + c

# print(total)

# a = [0,0,0]
# a[0] = int(input("수입력: "))
# a[1] = int(input("수입력: "))
# a[2] = int(input("수입력: "))

# total = a[0] + a[1] + a[2]

# print(total)

# list = ["빨강","노랑","초록","파랑"]
# list[2] = ""
# print(list)

# a = input("수입력: ")
# b = a[-1]

# if b == "0" or b == "2" or b == "4" or b == "6" or b == "8":
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 홀수".format(a))

# a = input("수입력: ")
# b = a[-1]

# if b in "02468":
#     print("{}는 짝수 입니다".format(a))
# else:
#     print("{}는 홀수 입니다".format(a))

# list = [300,30,333,"문자열",True]
# print(list)
# print(list[0])
# print(list[1])
# print(list[1:4])



# a = input("수입력: ")
# b = a[-1]

# if b in "02468":
#     print("{}는 짝수".format(a))
# else:
#     print("{}는 홀수".format(a))

# list = [300,30,333,"문자열",True]
# # 문자열
# print(list[3])

# # 문
# print(list[3][0])

# A = ["red","green","yellow","apple","is","delicious"]

# print(A[0],A[3],A[4],A[5])

# A = [["a","p","p","l","e"],["python","is","funny"],["happy","new","year"]]
# B = ["apple"]

# # print(A[0][0],A[0][1],A[0][2],A[0][2],A[0][3],A[0][4])
# print(A[1][0],A[1][1],A[1][2])
# print(A[2][0],A[2][1],A[2][2])
# print(B[0][0],B[0][1],B[0][2],B[0][3],B[0][4])

# C = "안녕하세여"
# for문 사용
# print(len(A))
# print(len(B))
# print(len(B[0]))
# # print(len(C))

# # A -> for문

# for i in range(len(A)): # 3
#     for j in range(len(A[i])): # 5,3,5
#         print(A[i][j],end=" ")
#     print()

# # B -> for문

# for i in range(len(B[0])):
#     print(B[0][i],end=" ")
# print()

# # B -> 중첩 for문

# for i in range(len(B)): # 1
#     for j in range(len(B[0])): # 5
#         print(B[i][j],end=" ")
#     print()


# A = [["a","p","p","l","e"],["python","is","funny"],["happy","new","year"]]
# B = ["apple"]

# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j],end="")

        
# for i in range(len(B[0])):
#     print(B[0][i],end=" ")
# print()

# for i in range(len(B)):
#     print(B[i],end=" ")
# print()

# colors = ['black','blue','yellow','red']
# for color in colors:
#     print(color,len(color))

# A = [["a","p","p","l","e"],
#     ["python","is","funny"],
#     ["happy","new","year","HI","BYE"]]

# B = ["apple"]

# print(len(B))
# # 반복문 + len함수 사용

# # A -> for문
# for i in range(len(A)): # 3
#     for j in range(len(A[i])): # 5,3,5
#         print(A[i][j],end=" ")
#     print()

# # B -> for문
# for i in range(len(B[0])):
#     print(B[0][i],end=" ")
# print()

# B -> 중첩 for문
# for i in range(len(B)): # 1
#     for j in range(len(B[0])): # 5
#         print(B[i][j],end=" ")
#     print()

# for i in range(len(B)):
#     for j in range(len(B[0])):
#         print(B[i][j],end=" ")
#     print()


# A = [["a","p","p","l","e"],
#     ["python","is","funny"],
#     ["happy","new","year"]]

# B = ["apple"]


# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j],end=" ")
#     print()

# # for i in range(len(B[0])):
#     print(B[0][i],end=" ")

# # B -> for문
# for i in range(len(B[0])):
#     print(B[0][i],end=" ")
# print()




# for i in range(len(B)):
#     for j in range(len(B[0])):
#         print(B[i][j],end=" ")
#     print()


# for i in range(len(B)): # 1
#     for j in range(len(B[0])): # 5
#         print(B[i][j],end=" ")
#     print()

# a = [1,2,3,4]
# sum1 = a[0]+a[1]+a[2]+a[3]
# print(sum1/4)


# list_a = ["A","B","C"]

# list_a.append("D")
# print(list_a)

# list_a.insert(0,"F")
# print(list_a)

# list_a.extend(["H","I","J"])
# print(list_a)

# del list_a[0]
# print(list_a)

# list_a.pop(2)
# print(list_a)

# list_a.pop()
# print(list_a)

# del list_a[0:2]
# print(list_a)

# list_a.remove("H")
# print(list_a)

# list_a.clear()
# print(list_a)

# A = [0,1,2,3,4,5,6,7,8,9]

# A.append(10)
# print(A)

# a = [200,101,5,32,64,9,72,900,99]
# for i in a:
#     if i >= 100:
#         if i % 2 == 0:
#             print("{}는 100 이상이며 짝수".format(i))
#         else:
#             print("{}는 100 이상이며 홀수".format(i))


# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     print("{}의 자릿수는: {} 입니다".format(i,len(str(i))))

# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# b = [[],[],[]]

# for i in a:
#     b[(i+2)%3].append(i)
# print(b)

# dict_a = {"name":"펭수","age":20}
# print(dict_a)
# print(dict_a["name"])


# dict_c = {
#     "name":"펭수",
#     "age":20,
#     "workmate": ["뚝딱이","범이","뿡뿡이","번개맨","EBS사장님"],
#     "birthplace":"남극"
# }
# dict_c["food"]="갈비"
# print(dict_c)

# dict_c["food"]="동원참치"
# print(dict_c)

# del dict_c["food"]
# print(dict_c)


#숙제 (10명의 평균 점수 데이터) => 평균 점수의 총합

# avr = [[90,80,70],[91,81,71],[92,82,72],[93,83,73],[94,84,74],
# [95,85,75],[96,86,76],[97,87,77],[98,88,78],[99,89,79]]
# b = [[[],[],[]]]

# #평균 점수 구하기(10명)
# # avr1 = avr[0][0]+avr[0][1]+avr[0][2]+avr[1][0]+avr[1][1]+avr[1][2]
# # print(avr1)

# for i in range(len(avr)):
    

#총합(10명의 평균의 총합)


# a = [1,2,3,4,5,6,7,8,9,10,11,12]

# a.append(13)
# print(a)

# a.insert(0,0)
# print(a)

# a.extend([14,15,16])
# print(a)

# del a[16]
# print(a)

# a.pop(15)
# print(a)

# a.remove(13)
# a.remove(14)
# print(a)

# a.clear()
# print(a)


# dict_a = {"name":"이지수", "age":"26"}
# print(dict_a)
# print(dict_a["name"])
# dict_a["drink"]="coffee"
# print(dict_a)

# list_1 = [300,30,333,"문자열",True]
# print(list_1[0])
# print(list_1[1])
# print(list_1[2])

# print(list_1[1:3])
# print(list_1[0:4])

# print(list_1[-1])
# print(list_1[-2])

# a = [0,0,0]
# a[0] = int(input("수입력: "))
# a[1] = int(input("수입력: "))
# a[2] = int(input("수입력: "))
# total = a[0] + a[1] + a[2]
# print(total)

# fruit = ["사과","포도","복숭아","딸기"]
# fruit[0] = "메론"
# print(fruit)

# a = input("문자 입력: ")
# b = a[-1]

# if b == 0 or b == 2 or b == 4 or b == 6 or b == 8:
#     print("{}는 짝수".format(b))
# else:
#     print("{}는 홀수".format(b)

# a = input("문자 입력: ")
# b = a[-1]
# if b in "02468":
#     print("{}는 짝수".format(b))
# else:
#     print("{}는 홀수".format(b))

# list_2 = [[1,2,3],["넷","다섯","여섯"],[7,8,9]]
# print(list_2)

# list_3 = [300,"문자열",True]
# print(list_3)

# A = ["red","green","yellow","apple","is","delicious"]
# print(A[0],A[3],A[4],A[5])

# A = [["a","p","p","l","e"],
#     ["python","is","funny"],
#     ["happy","new","year","HI","BYE"]]

# B = ["apple"]

# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j],end=" ")
#     print()

# for i in range(len(B[0])):
#     print((B[0][i]),end=" ")
# print()


# for i in range(len(B)):
#     for j in range(len(B[0])):
#         print(B[i][j],end=" ")
#     print()

# list_a = ["A","B","C"]
# list_b = ["D","E","F","G","H"]
# print(list_a + list_b)
# print(list_a*3)
# print(len(list_a))

# a = [1,2,3,4]
# print(sum(a))
# print(len(a))
# print(sum(a)/len(a))

# sum = a[0] + a[1] + a[2] + a[3]
# print(sum/4)

# list_a = ["A","B","C"]
# list_a.append("D")
# list_a.insert(1,"E")
# list_a.extend(["바보","멍청이"])
# del list_a[1:6]
# list_a.pop()

# print(list_a)
# list_b = [1,2,3,1,2,3,1,2,3]
# list_b.remove(1)
# print(list_b)
# list_a.remove("A")
# print(list_a)

# for i in range(3):
#     list_b.remove(1)
# print(list_b)

# list_b.clear()
# print(list_b)

# list_1 = [273,32,103,57,52]
# for i in list_1:
#     print(i,end= " ")
# print()

# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     if i >= 100:
#         if i % 2 == 0:
#             print("100 이상의 짝수: {}".format(i))
#         else:
#             print("100 이상의 홀수: {}".format(i))

# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     for j in len(a):
#         print("{} 자리수는 {} 입니다".format(a,len(str(i))))


# a = [1,2,3,4,5,6,7,8,9,10,11,12]
# b = [[],[],[],[]]

# for i in a:
#     b[(i+2)%3].append(i)
# print(b)


# for i in a:
#     b[(i+3)%4].append(i)
# print(b)


# list_a = [0,1,2,3,4,5,6,7]

# list_a.extend(list_a)
# print(list_a)

# list_a.append(10)
# print(list_a)

# list_a.insert(3,0)
# print(list_a)

# list_a.remove(3)
# print(list_a)

# list_a.pop(3)
# print(list_a)

# list_a.clear()
# print(list_a)

# numbers = [273,103,5,32,65,9,72,800,99]

# # for number in numbers:
# #     if number >= 100:
# #         print("100 이상의 수: {}".format(number))

# for number in numbers:
#     print("{}는 {}자리 입니다".format(number,len(str(number))))

# list_of_list= [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9]
# ]

# for a in list_of_list:
#     for b in a:
#         print(b)


# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]

# for number in numbers:
#     output[(number - 1)%3].append(number)
# print(output)

# n = input("문자 입력: ")
# b = n[-1]

# if b in "02468":
#     print("{}는 짝수".format(n))
# # else:
# #     print("{}는 홀수".format(n))


# # A = ["red","green","yellow","apple","is","delicious"]

# # print(A[0],A[3],A[4],A[5])

# A = [["a","p","p","l","e"],["python","is","funny"],["happy","new","year"]]
# B = ["apple"]

# # print(A[0][0],A[0][1],A[0][2],A[0][3],A[0][4])
# # print(A[1][0],A[1][1],A[1][2])
# # print(A[2][0],A[2][1],A[2][2])
# # print(B[0][0],B[0][1],B[0][2],B[0][3],B[0][4])

# # for i in range(len(A)):
# #     for j in range(len(A[i])):
# #         print(A[i][j],end=" ")
# #     print()

# # for i in range(len(B)):
# #     for j in range(len(B[0])):
# #         print(B[i][j],end=" ")
# #     print()

# # a = [1,2,3,4]
# # sum = a[0]+a[1]+a[2]+a[3]
# # avr = sum/4
# # print(avr)

# list_a = ["A","B","C"]
# # list_a.append("D")
# # print(list_a)
# list_a.insert(0,"E")
# print(list_a)

# list_a.extend(["D","E","F"])
# print(list_a)

# del list_a[4]
# print(list_a)

# list_a.pop(0)
# print(list_a)

# list_a.remove("A")
# print(list_a)

# list_a.clear()
# print(list_a)


# list_1 = [273,32,103,57,52]

# for i in list_1:
#     print(i) 

# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     if i > 100:
#         if i % 2 == 0:
#             print("{}는 짝수".format(i))
#         else:
#             print("{}는 홀수".format(i))


# a = [200,101,5,32,64,9,72,900,99]

# for i in a:
#     print("a의 자리수는 {} 입니다".format(len(str(i))))


a = [1,2,3,4,5,6,7,8,9,10,11,12]
b = [[],[],[],[]]

for i in a:
    b[(i+3)%4].append(i)
print(b)
