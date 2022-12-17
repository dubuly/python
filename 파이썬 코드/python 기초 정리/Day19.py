# 문제 5

# print 사용

# def 약수(n):
#     for i in range(1,n+1):
#         if n % i == 0:
#             print("약수: {}".format(i),end=" ")
# 약수(8)

# return 사용(값이 참일때 바로 종료되는 특징을 가지고 있음)

# def 약수(n):
#     b = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             b.append(i)
#     return(b)

# print(약수(8))

# 함수 용어 정리

# 호출: 함수를 실행
# 매개변수: 함수 괄호 안에 넣는것을 의미
# 리턴값: 함수의 최종적인 결과를 의미


# 튜플: 함수와 함께 사용되는 자료형으로, 리스트와 비슷하지만 한번 결정된 요소는 변경 불가
# (데이터, 데이터, 데이터, ...)


# tuple = (10,20,30)

# print(tuple[0])
# print(tuple[1])
# print(tuple[2])

# 튜플의 이상한 사용법

# # 요소 변경 불가능

# tuple[0] = 100

# print(tuple)

# 요소 교환

# a,b = (10,20)

# print("요소 교환 전: {}\t{}".format(a,b))

# a,b = b,a

# print("요소 교환 전: {}\t{}".format(a,b))


# # 요소를 하나만 가지는 튜플(하나만 사용시 , 붙임)

# a = (273,)

# print(a[0])


# # 멤버 연산자 사용(숫자에는 , 사용)

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

# 튜플 + 함수

# def test():
#     return 10,20

# a,b = test()

# print(a)
# print(b)
# print(test())



# 지역 변수 : 함수 내에서만 유효한 변수

# 전역 변수 : 함수에 상관 없이 코드 내에서 사용할 수 있는 변수

# 전역 변수
# a = 10
# def 전역변수():
#     print(a)

# 전역변수()

# print(a)


# 지역 변수
# def 지역변수():

#     a = 10

#     print(a)

# 지역변수()

# print(a)


# global 키워드 (지역 -> 전역)

# def 지역변수():
#     global a
#     a = 10

#     print(a)

# 지역변수()

# print(a)


# 함수 정리 문제 1

# def 문제1():
#     print("안녕하세요")
# 문제1()


# 문제 2

# a = int(input("수입력: "))

# def 문제2(a):
#         if a % 2 == 0:
#             print("{}는 짝수".format(a))
#         else:
#             print("{}는 홀수".format(a))
# 문제2(a)

# return

# def 문제2(a):
#         if a % 2 == 0:
#             return "{}는 짝수".format(a)
#         else:
#             return "{}는 홀수".format(a)


# a = int(input("수입력: "))

# print(문제2(a))



# 문제 3

# a = int(input("수입력: "))
# b = int(input("수입력: "))

# def 문제3():
#     sum1 = a + b
#     print("두 수의 합: {}".format(sum1))
# 문제3()


# a = int(input("수입력: "))
# b = int(input("수입력: "))

# def 문제3(a,b):
#     return "두 수의 합: {}".format(a+b)
# 문제3(a,b)



# 문제 4

# a = int(input("수입력: "))

# def 문제4(a):
#     if a % 7 == 0:
#         return "{}는 7의 배수".format(a)
#     else:
#         return "{}는 7의 배수가 아니다".format(a)
# print(문제4(a))


# 문제 5

# def 문제5(a):
#     r_a = ""
#     for i in a:
#         r_a = i + r_a

#     return r_a

# a = input("문자 입력: ")

# print(문제5(a))


# 용어 정리
# 윈도우: 컴퓨터엥서 띄우는 창을 윈도우라 명칭
# 위젯: 위젯의 사전적 의미는 '소형 장치' 또는 '부품'으로 사용자가 사용할 수 있도록 기능만을 모아 놓은 도구 모음
# 엔트리: 입력창으로 사용자로 부터 값을 입력받을 수 있는 창


# tkinter

# 1. 창 생성

# 호출
# from  tkinter import *

# window = Tk()

# window.mainloop()

# 2. 버튼 생성

# from  tkinter import *

# window = Tk()

# button = Button(window,text="클릭하세요!")

# button.pack()

# window.mainloop()

# 3. 레이블과 엔트리 위젯 사용

# from  tkinter import *

# window = Tk()

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨 -> 섭씨")
# l2 = Label(window,text="섭씨 -> 화씨")

# l1.pack()
# l2.pack()


# window.mainloop()

# # Entry(사용자로부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.pack()
# e2.pack()

# window.mainloop()

# b1 = Button(window,text="화씨 -> 섭씨")
# b2 = Button(window,text="섭씨 -> 화씨")

# b1.pack()
# b2.pack()

# window.mainloop()


# 버튼 만들기
# from tkinter import *

# window = Tk()
# window.title("버튼 생성 실습")
# window.geometry("200x150") # 가로,세로 너비 설정


# l1 = Label(window,text="*** 버튼 2개 만들기 ***")
# l1.pack()

# button1 = Button(window,text="1번 버튼")
# button2 = Button(window,text="2번 버튼")

# button1.pack()
# button2.pack()

# window.mainloop()


# 배치 관리자

# from  tkinter import *

# window = Tk()

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨 -> 섭씨")
# l2 = Label(window,text="섭씨 -> 화씨")

# l1.pack()
# l2.pack()


# 격자 배치 관리자

# from  tkinter import *

# window = Tk()

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨")
# l2 = Label(window,text="섭씨")

# l1.grid(row=0,colum=0)
# l2.grid(row=1,colum=0)


# window.mainloop()

# # Entry(사용자로부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0,colum=1)
# e2.grid(row=1,colum=1)

# window.mainloop()

# b1 = Button(window,text="화씨 -> 섭씨")
# b2 = Button(window,text="섭씨 -> 화씨")

# b1.grid(row=0,colum=2)
# b2.grid(row=1,colum=2)


# window.mainloop()


# 5. 버튼 이벤트 처리

# from  tkinter import *

# window = Tk()

# def process():
#     print("오늘은 10월 4일 입니다.")


# button = Button(window,text="클릭하세요!",command=process)

# button.pack()

# window.mainloop()


# 6. 버튼에 함수 연결

# from  tkinter import *

# window = Tk()

# def process1():
#     e2.insert(0,100)

# # Label(화면에 텍스트 표시)
# l1 = Label(window,text="화씨")
# l2 = Label(window,text="섭씨")

# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)


# window.mainloop()

# Entry(사용자로부터 값을 입력 받음)

# e1 = Entry(window)
# e2 = Entry(window)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# window.mainloop()

# b1 = Button(window,text="화씨 -> 섭씨")
# b2 = Button(window,text="섭씨 -> 화씨")

# b1.grid(row=0,column=2)
# b2.grid(row=1,column=2)


# window.mainloop()



# 화씨 -> 섭씨 변환 프로그램

from  tkinter import *

window = Tk()

def process1():
    e2.insert(0,100)

def process1():
    섭씨 = float(e1.get())
    화씨 = 섭씨 * 1.8 + 32
    e1.insert(0,화씨)


def process2():
    화씨 = float(e1.get())
    섭씨 = (화씨 - 32) / 1.8
    e2.insert(0,섭씨)


def process3():
    e1.delete(0,30)
    e2.delete(0,30)
    

# Label(화면에 텍스트 표시)
l1 = Label(window,text="화씨")
l2 = Label(window,text="섭씨")

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)


window.mainloop()

# Entry(사용자로부터 값을 입력 받음)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=1,column=0)
e2.grid(row=1,column=1)

window.mainloop()

b1 = Button(window,text="화씨 -> 섭씨")
b2 = Button(window,text="섭씨 -> 화씨")

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)



# 초기화
b3 = Button(window,text="초기화",command=process3)
b3.grid(row=2,column=2)





window.mainloop()