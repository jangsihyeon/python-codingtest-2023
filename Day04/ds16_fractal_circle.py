# 프렉탈 원 그리기
import turtle         # 그림그려주는 거북이
import tkinter as tk
t = turtle.Turtle()   # 거북이 만들기
t.shape('turtle')

turtle.setup(width=600, height=600)
c = t.clone()         # 거북이 만들기
c.color('red')
c.circle(30)

for i in range(4, 10):
    c.circle(i*10)

turtle.mainloop()
