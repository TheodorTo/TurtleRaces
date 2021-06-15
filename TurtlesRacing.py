import turtle
import random
from tkinter import *
from tkinter import messagebox

window = Tk()

turtle1 = turtle.Turtle()

gamer1 = turtle.Turtle()
gamer2 = turtle.Turtle()
gamer3 = turtle.Turtle()
gamer4 = turtle.Turtle()

gamer1steps=0
gamer2steps=0
gamer3steps=0
gamer4steps=0

gamer1win=0
gamer2win=0
gamer3win=0
gamer4win=0

a=0
def line(x):
    turtle1.speed(100)
    turtle1.penup()
    turtle1.goto(x, 100)
    turtle1.write(i)
    turtle1.rt(90)
    turtle1.pendown()
    turtle1.fd(300)
    turtle1.left(90)
    turtle1.penup()


x = -250

for i in range(0, 26):
    line(x)
    x = x+20
gamer1.pencolor('green')
gamer1.penup()
gamer1.goto(-250, 80)
gamer1.shape('turtle')
gamer1.pendown()

gamer2.pencolor('blue')
gamer2.penup()
gamer2.goto(-250, 0)
gamer2.shape('turtle')
gamer2.pendown()

gamer3.pencolor('yellow')
gamer3.penup()
gamer3.goto(-250, -80)
gamer3.shape('turtle')
gamer3.pendown()

gamer4.pencolor('red')
gamer4.penup()
gamer4.goto(-250, -160)
gamer4.shape('turtle')
gamer4.pendown()

while a == 0:

    gamer1steps = random.randint(0, 10)
    gamer2steps = random.randint(0, 10)
    gamer3steps = random.randint(0, 10)
    gamer4steps = random.randint(0, 10)

    gamer1.fd(gamer1steps)
    gamer2.fd(gamer2steps)
    gamer3.fd(gamer3steps)
    gamer4.fd(gamer4steps)

    if gamer1.pos() > (270, 80):
        a = 1
        gamer1win = 1
    if gamer2.pos() > (270, 0):
        a = 1
        gamer2win = 1
    if gamer3.pos() > (270, -80):
        a = 1
        gamer3win = 1
    if gamer4.pos() > (270, -160):
        a = 1
        gamer4win = 1

if gamer1win == 1:
    messagebox.showinfo("Info Popup", "green win")
elif gamer2win == 1:
    messagebox.showinfo("Info Popup", "blue win")
elif gamer3win == 1:
    messagebox.showinfo("Info Popup", "yellow win")
elif gamer4win == 1:
    messagebox.showinfo("Info Popup", "red win")

turtle.done()
window.mainloop()
