#print("test!! (commit-ability test)")
#print("test 2 commit-ability test!!")
print("COMMIT TEST 3!!!!)")
import time

name = input("Name your character:  ")
time.sleep(0.2)
print("Hello, " + name)
time.sleep(0.05)
print("---")
time.sleep(0.05)
print("Launching interactive window... ")
time.sleep(2)

a_status = "false"
b_status = "false"
c_status = "false"
d_status = "false"
e_status = "false"
f_status = "false"

p_status = "false"

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

def a_key(): #spikey triangles
    global a_status 
    a_status = "true"
    #a.write("star", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(1.5)
    a.clear
    a.color("blue")
    a.fillcolor("green")
    a.begin_fill()
    a.forward(50)
    a.right(45)
    a.forward(50)
    a.right(270)
    a.forward(75)
    a.right(145)
    a.forward(75)
    a.right(120)
    a.forward(75)
    a.end_fill()
    time.sleep(1.5)

screen.onkey(a_key, "a")
screen.listen()
    
def b_key(): #circular-nodes
    global b_status 
    b_status = "true"
    #b.write("bear", align = "center", font = ("Verdana", 15, "normal"))
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

screen.onkey(b_key, "b")
screen.listen()

def c_key(): #rectangles
    global c_status 
    c_status = "true"
    #c.write("Candles!", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(1.5)
    c.clear()
    screen.bgcolor("black")
    c.goto(-100, -200)
    c.pendown()
    c.fillcolor("white")
    c.begin_fill()
    c.forward(20)
    c.right(90)
    c.forward(100)
    c.right(90)
    c.forward(20)
    c.right(90)
    c.forward(100)
    c.end_fill()
    c.penup()
    c.setheading(0)
    c.goto(-100, -200)
    c.right(90)
    c.forward(100)
    c.left(90)
    c.pendown()
    c.fillcolor("yellow")
    c.begin_fill()
    c.forward(25) #start candle 2
    c.left(90)
    c.forward(73)
    c.left(90)
    c.forward(8)
    c.left(90)
    c.forward(73)
    c.left(90)
    c.forward(8)
    c.end_fill()
    c.penup()
    c.goto(-75, -80)
    c.pendown()
    #c.fillcolor("white")
    #c.begin_fill()

screen.onkey(c_key, "c")
screen.listen()

def p_key():
    global p_status 
    p_status = "true"
    p.write("Polka dots!", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(1.5)
    p.clear()
    p.color("black")
    p.goto(-100, -220)
    p.dot(20)
    p.goto(-50, 3)
    p.color("blue")
    p.dot(6)
    p.color("yellow")
    p.goto("300, -4")
    p.dot(7)
    p.goto(50, 74)
    p.color("orange")
    p.dot(14)
    time.sleep(1.5)

screen.onkey(p_key, "p")
screen.listen()



#that was a useless/redundant line mb



turtle.done()
