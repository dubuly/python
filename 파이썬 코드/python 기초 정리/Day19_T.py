# 문제5

# # print 사용
# def 약수1(a):

#     for i in range(1,a+1):
#         if a % i == 0:
#             print("{}은 약수".format(i))

# 약수1(8)


# # return 사용
# def 약수1(a):
#     b = []
#     for i in range(1,a+1):
#         if a % i == 0:
#             b.append(i)
#     return b

# print(약수1(8))


# # 튜플 (tuple)

# tuple1 = (10,20,30)

# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])

# 튜플의 이상한 사용법

# # 요소 변경 -> TypeError
# tuple1[0] = 100

# print(tuple1)

# # 요소 교환

# a,b = (10,20)

# print("요소 교환 전 : {}\t{}".format(a,b))

# a,b = b,a

# print("요소 교환 전 : {}\t{}".format(a,b))

# # 요소를 하나만 가지는 튜플
# a = (273,)

# print(a[0])

# # *** 멤버 연산자 ***

# # 문자
# print("가" in "가")
# print("가" in ("가","나","다"))

# # 정수
# print(1 in (1,))
# print(1 in (1,2,3))


# # 리스트와 튜플의 이상한 사용법
# [a,b] = [10,20]
# (c,d) = (30,40)

# print("{} {} {} {}".format(a,b,c,d))


# # 괄호가 없는 튜플
# a = 10,20,30,40,50

# print(a)
# print(type(a))


# # 튜플 + 함수

# def test():
#     return (10,20)

# a,b = test()

# print(a)
# print(b)
# print(test())


# 지역 변수 : 함수 내에서만 유효한 변수

# 전역 변수 : 함수에 상관없이 코드 내에서 사용할 수 있는 변수


# # 전역 변수
# a = 10

# def 전역변수():
#     print(a)

# 전역변수()

# print(a)


# # 지역 변수
# def 지역변수():

#     a = 10

#     print(a)

# 지역변수()

# print(a)


# # global 키워드 (지역 변수 -> 전역 변수)

# def 지역변수():
#     global a 
#     a = 10

#     print(a)

# 지역변수()

# print(a)


# # 문제1

# def 인사():
#     print("안녕하세요")

# 인사()

# # 문제2

# def 홀짝(a):

#     if a % 2 == 0:
#         return "{}은 짝수".format(a)

#     else:
#         return "{}은 홀수".format(a)

# a = int(input("수입력: "))

# print(홀짝(a))

# # 문제3

# a = int(input("수입력: "))
# b = int(input("수입력: "))

# def 합(a,b):
#     return "합 : {}".format(a+b)

# print(합(a,b))

# # 문제4

# def 배수(a):

#     if a % 7 == 0:
#         return "{}은 7의 배수 입니다.".format(a)

#     else:
#         return "{}은 7의 배수가 아닙니다.".format(a)

# a = int(input("수입력: "))

# print(배수(a))


# # 문제5
# def 우영우(a):

#     r_a = ""
#     for i in a:
#         r_a = i + r_a
#     return r_a

# a = input("입력: ")

# print(우영우(a))


# tkinter

# # 1. 창생성

# from tkinter import *

# window = Tk()

# window.mainloop()

# # 2. 버튼 생성

# from tkinter import *

# window = Tk()

# button = Button(window,text="클릭하세요!")

# button.pack()

# window.mainloop()


# # 3. 레이블과 엔트리 위젯 사용

# from tkinter import *

# window = Tk()

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨 -> 섭씨")
# l2 = Label(window,text="섭씨 -> 화씨")

# l1.pack()
# l2.pack()

# # Entry(사용자로 부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.pack()
# e2.pack()

# # Button (버튼)
# b1 = Button(window,text="화씨 -> 섭씨")
# b2 = Button(window,text="섭씨 -> 화씨")

# b1.pack()
# b2.pack()

# window.mainloop()


# # 실습
# from tkinter import *

# window = Tk()
# window.title("버튼 생성 실습")
# window.geometry("200x150")

# l1 = Label(window,text="*** 버튼 2개 만들기 ***")
# l1.pack()

# b1 = Button(window,text="1번 버튼")
# b2 = Button(window,text="2번 버튼")
# b1.pack()
# b2.pack()

# window.mainloop()


# # 4. 격자 배치 관리자

# from tkinter import *

# window = Tk()

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨")
# l2 = Label(window,text="섭씨")

# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)

# # Entry(사용자로 부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# # Button (버튼)
# b1 = Button(window,text="화씨 -> 섭씨")
# b2 = Button(window,text="섭씨 -> 화씨")

# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# window.mainloop()


# # 5. 버튼 이벤트 처리

# from tkinter import *

# window = Tk()

# def process():
#     print("오늘은 10월 4일 입니다.")

# button = Button(window,text="클릭하세요!",command=process)

# button.pack()

# window.mainloop()



# # 6. 버튼에 함수 연결

# from tkinter import *

# window = Tk()

# def process1():
#     e2.insert(0,100)

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨")
# l2 = Label(window,text="섭씨")

# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)

# # Entry(사용자로 부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# # Button (버튼)
# b1 = Button(window,text="화씨 -> 섭씨",command=process1)
# b2 = Button(window,text="섭씨 -> 화씨")

# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# window.mainloop()


# # 7. 화씨 -> 섭씨 변환 프로그램 제작

# from tkinter import *

# window = Tk()

# def process1():
#     화씨 = float(e1.get())
#     섭씨 = (화씨 - 32) /1.8
#     e2.insert(0,섭씨)

# def process2():
#     섭씨 = float(e2.get())
#     화씨 = 섭씨 * 1.8 + 32
#     e1.insert(0,화씨)

# def process3():
#     e1.delete(0,30)
#     e2.delete(0,30)

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨")
# l2 = Label(window,text="섭씨")

# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)

# # Entry(사용자로 부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# # Button (버튼)
# b1 = Button(window,text="화씨 -> 섭씨",command=process1)
# b2 = Button(window,text="섭씨 -> 화씨",command=process2)

# b1.grid(row=2,column=0)
# b2.grid(row=2,column=1)

# # 초기화
# b3 = Button(window,text="초기화",command=process3)
# b3.grid(row=2,column=2)


# window.mainloop()


