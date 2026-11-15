#print("test!! (commit-ability test)")
#print("test 2 commit-ability test!!")
print("COMMIT TEST 3!!!!)")
import random
import time

name = input("Name your character:  ")
time.sleep(0.2)
print("Hello, " + name)
time.sleep(0.05)
print("---")    
time.sleep(0.05)
print("===")
time.sleep(0.05)
global delay
global sleep
delay = input("Delay drawings?")
if delay == "y":
    sleep = 1.5
if delay == "n":
    sleep = 0
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
d = turtle.Turtle()
e = turtle.Turtle()

t.showturtle()
t.color("red")
t.forward(100)
t.write(name, align = "center", font = ("Impact", 20, "underline"))

#list for ALL turtles' "randomized" coordinates:
global y_location
global x_location
global x_choices
global y_choices
x_choices = [-10, -20, -30, -40, -45, 53, 28, 27, -94, 333, -333, 18, 10, 20, 30, 40 ,50 ,45, 60, 90]
x_location = random.choice(x_choices)  #typo was z_location. There is no "z".
y_choices = [20, 29, 23, 92, -91, -3, -5, -257, 283, 87, -11, -52, -220, 323, 49, -34, -34 , -116, 200]
y_location = random.choice(y_choices)

#random fillcolors:
global colors
global color_bank
color_bank = ["blue", "green", "red", "purple", "white", "black", "yellow", "pink", "orange", "brown"]
colors = random.choice(color_bank)

#random direction (turning right):
global direction
global turn
global degrees
degrees = (0, 360)
turn = random,choice(degrees)
direction = random.choice(turn)

#move-by distance:
global distance
global move
global distance_list
distance_list = range(1, 250)
move = random.choice(distance_list)
distance = random.choice(move)

def a_key(): #spikey triangles
    global a_status 
    a_status = "true"
    #a.write("star", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(sleep)
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
    time.sleep(sleep)
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
    time.sleep(sleep)  #used to be time.sleep(1.5)
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


def d_key():  #failed star again lol
    global d_status
    d_status = "true"
   # d.write("something, idk")
    time.sleep(sleep)
    d.color("yellow")
    for stars in range(3):
        d.penup()
        d.goto(x_location, y_location)
        d.pendown()
        d.fillcolor("yellow")
        d.begin_fill()
        d.forward(100) 
        d.right(135)
        d.forward(100)
        d.right(115) #or 135
        d.forward(100)
        d.right(45)
        d.forward(100)
        d.right(45)
        d.forward(100)
        d.end_fill()

screen.onkey(d_key, "d")
screen.listen()

def e_key():
    global e_status
    global colors
    global color_bank
    e_status = "true"
    #e.write()
    time.sleep(sleep)
    e.clear()
    e.penup()
    e.fillcolor(colors)
    #e.goto(x_location, y_location)
    e.pendown()
    e.begin_fill()
    e.forward(50)
    e.right(90)
    e.forward(70)
    e.right(90)
    e.forward(50)
    e.right(90)
    e.forward(70)
    e.penup()
    e.end_fill()
    e.goto(x_location, y_location)
    e.fillcolor(colors)
    e.begin_fill()
    e.pendown()
    e.forward(50) #hopefully a star
    e.right(115)
    e.forward(59)
    e.right(115)
    e.forward(50)
    e.right(115)
    e.forward(50)
    e.right(115)
    e.forward(50)
    e.right(115)
    e.forward(50)
    e.right(115)
    e.forward(50)
    e.penup()
    e.end_fill()

screen.onkey(e_key, "e")
screen.listen()

def f_key():
    global f_status
    f_status = "true"
    #f.write()
    time.sleep(sleep)
    f.penup()
    f.goto(x_locaiton, y_location)
    f.pendown()
    f.fillcolor(colors)
    f.begin_fill()
    f.turn(turn)
    f.forward(move)

def p_key():
    global p_status 
    p_status = "true"
   # p.write("Polka dots!", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(sleep)
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
