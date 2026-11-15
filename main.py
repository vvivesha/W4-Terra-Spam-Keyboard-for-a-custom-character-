#print("test!! (commit-ability test)")
#print("test 2 commit-ability test!!")
import time

name = input("Name your character:  ")
time.sleep(0.2)
print("Hello, " + name)
time.sleep(0.05)
print("---")
time.sleep(0.05)
print("Launching interactive window... ")
time.sleep(2)

a = "false"
b = "false"
c = "false"
d = "false"
e = "false"
f = "false"

p = "false"

import turtle
screen = turtle.Screen()
p = turtle.Turtle()
t = turtle.Turtle()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()

t.showturtle()
t.color("red")
t.forward(100)
t.write(name, align = "center", font = ("Impact", 20, "underline"))

def a_key():
    global a 
    a = "true"
    a.write("star")
    time.sleep(1.5)
    a.clear
    a.color("blue")
    a.fillcolor("green")
    a.beginfill()
    a.forward(50)
    a.right(45)
    a.forward(50)
    a.right(270)
    a.forward(75)
    a.right(145)
    a.forward(75)
    a.right(120)
    a.forward(75)
    a.endfill()
    time.sleep(1.5)

screen.onkey(a, "a")
screen.listen()
    
def b_key():
    global b 
    b = "true"
    b.write("bear")
    b.goto(0, -100) #head
    b.color("brown")
    b.dot(50)
    b.goto(-50, -50) #left ear
    b.dot(15)
    b.goto(50, -50) #right ear
    b.dot(15)
    b.goto(15, -25) #right eye
    b.color("black")
    b.dot(5)
    b.goto(-15, -25) #left eye
    b.dot(5)
    time.sleep(1.5)

screen.onkey(b, "b")
screen.listen()

def c_key():
    global c 
    c = "true"
    c.write("Candles!")
    time.sleep(1.5)
    c.clear()
    screen.bgcolor("black")
    c.goto(-100, -200)
    c.pendown()
    c.fillcolor("white")
    c.beginfill()
    c.forward(20)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.forward(20)
    c.right(90)
    c.forward(100)
    c.endfill()
    c.penup()
    c.setheading(0)
    c.goto(-100, -200)
    c.right(90)
    c.forward(100)
    c.left(90)
    c.pendown()
    c.fillcolor("yellow")
    c.beginfill()
    c.forward(25) #start candle 2
    c.left(90)
    c.forward(73)
    c.left(90)
    c.forward(8)
    c.left(90)
    c.forward(73)
    c.left(90)
    c.forward(8)
    c.endfill()
    c.penup()
    c.goto(-75, -80)
    c.pendown()
    c.fillcolor("white")
    c.beginfill()
    c.



def p_key():
    global p 
    p = "true"
    p.write("Polka dots!")
    time.sleep(1.5)
    p.clear()
    p.color("black")
    p.goto(-100, -220)
    p.dot(20)
    p.goto(-50, 3
    p.color("blue")
    p.dot(6)
    p.color("yellow")
    p.goto("300, -4")
    p.dot(7)
    p.goto(50, 74)
    p.color("orange")
    p.dot(14)
    time.sleep(1.5)

screen.onkey(p, "p")
screen.listen()



#that was a useless/redundant line mb



turtle.done()
