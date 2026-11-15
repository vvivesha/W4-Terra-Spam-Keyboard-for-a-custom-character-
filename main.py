#print("test!! (commit-ability test)")
#print("test 2 commit-ability test!!")
#print("COMMIT TEST 3!!!!)")
print("Raised-By-This-Computer Sim")
import random
import time
countdown = 3

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
print("============================================")
global game
global suppress_1
game = input("Would you like to enable minigames?  (y/n)")
if game == "no":
    suppress_1 = "true"
if game == "yes":
    suppress_1 = "false"
print("Launching interactive window... ")
time.sleep(2)

one_status = "false"
a_status = "false"
b_status = "false"
c_status = "false"
d_status = "false"
e_status = "false"
f_status = "false"
g_status = "false"

p_status = "false"

import turtle
screen = turtle.Screen()
q0 = turtle.Turtle()
q1 = turtle.Turtle()
q2 = turtle.Turtle()
p = turtle.Turtle()
q = turtle.Turtle()
t = turtle.Turtle()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f - turtle.Turtle()
g = turtle.Turtle()

q0.showturtle()
q0.color("red")
q0.forward(100)
q0.write(name, align = "center", font = ("Impact", 20, "underline"))

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
turn = random.choice(degrees)
#direction = random.choice(turn)

#move-by distance:
global distance
global move
global distance_list
distance_list = range(1, 250)
move = random.choice(distance_list)
#distance = random.choice(move)

#list for one_key():
global memory_game_script
global memory_prompt
memory_game_script = ["Draw 3 TRIANGLES and 2 CIRCLES-- in that order.", "Draw 2 squares, a circle, and a square", "Draw 1 circle, 1 triangle, and 1 square.", "Draw 4 trianges", "Draw 2 rectangles and 1 square."]
memory_prompt = random.choice(memory_game_script)

#number_randomizer:
global r_number
r_number = random.choice(range(1, 200))

def c_key():
    c.penup()
    c.goto(x_location, y_location)
    c.dot(r_number)

#minigames:
def memory_game():
    q1.clear()
    q0.penup()
    q0.goto(-200, -200)
    q0.write("r = rectangle, s = square, c = circle, t = triangle", align = "left", font = ("Courier New", 10, "underline"))
    if activated == ["one_key()", "game_msg_2())", "c_key()", "r_key()", "s_key()", "t_key()"]:


screen.onkey(c_key, "c")
screen.listen()

def one_key():
    global one_status
    global countdown
    one_status = "true"
    q1.penup()
    time.sleep(1)
    q1.clear()
    time.sleep(0.5)
    q1.color("black")
    q1.write("Let\'s play a... Memory Game!", align = "center", font = ("Courier New", 16, "underline"))
    time.sleep(1)
    q1.clear()
    screen.bgcolor("black")
    q1.color("white")
    q1.write(memory_prompt)
    time.sleep(1.5)
   # for countdown in range(3):
    #    q1.goto(0, -25)
    #    countdown -= 1
    #    q1.write(countdown, align = "center", font = ("Impact", 20, "bold"))
    #    q1.clear()
    #    q1.goto(0, 0)
    #    q1.write("Draw 3 RED TRIANGLES and 2 BLUE CIRCLES-- in that order.")
    #    time.sleep(1)
    
    #q1.clear()
    #time.sleep(1)
    #q1.goto(0, 0)
    #q1.write("Draw 3 RED TRIANGLES and 2 BLUE CIRCLES-- in that order.")
    #q1.goto(0, -30)
    #q1. write("GOOOOO!", align = "center", font = ("Impact", 30, "underline"))
    q1.goto(0, -20)
    q1.color("green")
    q1.write("Press r for rectangle, t for triangle, s for a square, or c for a circle.", align = "left", font = ("Verdana", 15, "normal"))
    global membory_game
    memory_game = "true"

if memory_game == "true":
    memory_game()

def game_msg_2():
    if suppress_1 == "false":
        time.sleep(0.5)
        q1.penup()
        q1.goto(0, 50)
        q1.pendown()
        q1.write("Would you like to play a game?", align = "center", font = ("Courier New", 14, "bold"))
        q1.penup()
        q1.goto(0, 75)
        q1.pendown()
        q1.write("Press 1 on your keyboard to play Memory Game!")

screen.onkey(one_key, "1")
screen.listen()

def two_key():
    q2.penup()
    q2.write("Blind Walk", align = "center", font = ("Courier New", 16, "underline"))
    time.sleep(1)
    q2.clear()
    #q2.



screen.onkey(two_key, "2")
screen.listen

#moved globalized variables from here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!










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

def g_key(): #rectangles
    global c_status 
    g_status = "true"
    #g.write("Candles!", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(sleep)  #used to be time.sleep(1.5)
    g.clear()
    screen.bgcolor("black")
    g.goto(-100, -200)
    g.pendown()
    g.fillcolor("white")
    g.begin_fill()
    g.forward(20)
    g.right(90)
    g.forward(100)
    g.right(90)
    g.forward(20)
    g.right(90)
    g.forward(100)
    g.end_fill()
    g.penup()
    g.setheading(0)
    g.goto(-100, -200)
    g.right(90)
    g.forward(100)
    g.left(90)
    g.pendown()
    g.fillcolor("yellow")
    g.begin_fill()
    g.forward(25) #start candle 2
    g.left(90)
    g.forward(73)
    g.left(90)
    g.forward(8)
    g.left(90)
    g.forward(73)
    g.left(90)
    g.forward(8)
    g.end_fill()
    g.penup()
    g.goto(-75, -80)
    g.pendown()
    #g.fillcolor("white")
    #g.begin_fill()

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
        if suppress_1 == "false":
            two_key()

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
