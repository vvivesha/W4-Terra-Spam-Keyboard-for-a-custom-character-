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

import turtle
p = turtle.Turtle()
t = turtle.Turtle()
a = turtle.Turtle()
b = turtle.Turtle()

t.showturtle()
t.color("red")
t.forward(100)
t.write(name, align = "center", font = ("Impact", 20, "underline"))

def a():
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

turtle.Screen().onkey(a, "a")
turtle.Screen().listen()
    
def b():
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

turtle.Screen().onkey(b, "b")
turtle.Screen().listen()

def p():
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

turtle.Screen().onkey(p, "p")
turtle.Screen().listen()



#that was a useless/redundant line mb



turtle.done()
