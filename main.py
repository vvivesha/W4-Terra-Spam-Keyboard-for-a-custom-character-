#print("test!! (commit-ability test)")
#print("test 2 commit-ability test!!")
#print("COMMIT TEST 3!!!!)")
print("Turtle Drawing Sandbox")
import random
import time
countdown = 3
global trail_size
trail_size = 5

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
word1 = input("What\'s your favorite letter? *press enter to skip these 3 questions*  ")
word2 = input("What\'s your favorite style? ")
word3 = input("What\'s your favorite plant? ")
#custom = input("Would you like to customize your name?   (y/n)")
#if custom == "y":

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

#deleted "status" variables because they are now unnecessary
import turtle
screen = turtle.Screen()
q0 = turtle.Turtle()
q1 = turtle.Turtle()
q2 = turtle.Turtle()

c = turtle.Turtle()
r = turtle.Turtle()
s = turtle.Turtle()
t = turtle.Turtle()

a = turtle.Turtle()
b = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()

user = turtle.Turtle()
bot = turtle.Turtle()
bot.shape("turtle")

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

global range1
global range2
global range3
global range4

range0 = (-200, 200)
range1 = random.choice(range0)
range2 = random.choice(range0)
range3 = random.choice(range0)
range4 = random.choice(range0)

global size
global size1
global size2
global size3

size = range(1, 200)
size1 = random.choice(size)
size2 = random.choice(size)
size3 = random.choice(size)

#random fillcolors:
global color1
global color2
global color3
global color4
global color5
global color6
global color_bank
global pick_color
color_bank = ["blue", "green", "red", "purple", "white", "black", "yellow", "pink", "orange", "brown"]
pick_color = random.choice(color_bank)
color1 = pick_color
color2 = random.choice(color_bank)
color3 = random.choice(color_bank)
color4 = random.choice(color_bank)
color5 = random.choice(color_bank)
color6 = random.choice(color_bank)

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
global quest_script
global memory_prompt
quest_script = ["Draw 3 TRIANGLES and 2 CIRCLES-- in that order.", "Draw 2 squares, a circle, and a square", "Draw 1 circle, 1 triangle, and 1 square.", "Draw 4 trianges", "Draw 2 rectangles and 1 square."]
memory_prompt = random.choice(quest_script)

#number_randomizer:
#global r_number
#global pick_r_number
#pick_r_number = random.choice(range(1, 200))
#r_number = pick_r_number
#global r1_number
#global pick_r1_number
#pick_r1_number = random.choice(range(1,200))
#r1_number = pick_r1_number

#customize user's turtle:

q2.penup()
q2.goto(-150, 150)
q2.write("Use arrow keys to move!", align = "left", font = ("Verdana", 10, "normal"))
q2.right(90)
q2.forward(25)
q2.write("Press i to go underwater", align = "left", font = ("Verdana", 10, "normal"))
q2.forward(35)
q2.write("Press v for a narrower trail and w for a wider trail", align = "left", font = ("Verdana", 10, "normal"))

def word_1():
    user.penup()
    user.backward(10)
    user.write(word1, align = "center", font = ("Imapact", size1, "underline"))

def word_2():
    user.penup()
    user.backward(10)
    user.write(word2, align = "center", font = ("Courier New", size2, "normal"))

def word_3():
    user.penup()
    user.backward(10)
    user.write(word3, align = "center", font = ("Verdana", size3, "bold"))

def bg1():
    user.color("yellow")
    screen.bgcolor("green")

def bg2(): #underwater
    user.color("white")
    screen.bgcolor("blue")
    u_dots()
    a.penup()
    a.goto(range1, range2)
    a.dot(15, "white")
    a.goto(range2, range3)
    a.dot(14, "white")
    a.goto(range1, range4)
    a.goto(range3, range1)
    for turtles in range(8):
        q1.penup()
        q1.goto(random.choice(x_choices), random.choice(y_choices))
        q1.shape("turtle")
        q1.color("green")
        q1.stamp()

def u_invisible():
    user.clear()
    time.sleep(0.1)

def u_dots():
    for dots in range(8):
        user.dot(8, color5)
        time.sleep(0.1)

screen.onkey(u_invisible, "y")
screen.listen()
screen.onkey(u_dots, "u")
screen.listen()
screen.onkey(bg2, "i")
screen.listen()
screen.onkey(bg1, "l")
screen.listen()
screen.onkey(word_1, "j")
screen.listen()
screen.onkey(word_2, "k")
screen.listen()
screen.onkey(word_3, "m")

user.color("blue")
user.speed(0)
user.width(5)

bot.color("red")
bot.speed(0.001)
bot.width(6)
bot.goto(-5, 5)

#right
def right():
    bot.pendown()
    user.pendown()
    user.setheading(0)
    user.forward(20)
    bot.setheading(0)
    bot.left(90)
    bot.forward(5)
    bot.right(180)
    bot.forward(5)
    bot.left(90)
    bot.forward(20)
    user.penup()
    bot.penup()

#left
def left():
    bot.pendown()
    user.pendown()
    user.setheading(180)
    user.forward(20)
    bot.setheading(180)
    bot.left(90)
    bot.forward(5)
    bot.right(180)
    bot.forward(5)
    bot.left(90)
    bot.forward(20)
    user.penup()
    bot.penup()

#down
def down():
    bot.pendown()
    user.pendown()
    user.setheading(270)
    user.forward(20)
    bot.setheading(270)
    bot.left(90)
    bot.forward(5)
    bot.right(180)
    bot.forward(5)
    bot.left(90)
    bot.forward(20)
    user.penup()
    bot.penup()

#up
def up():
    bot.pendown()
    user.pendown()
    user.setheading(90)
    user.forward(20)
    bot.setheading(90)
    bot.left(90)
    bot.forward(5)
    bot.right(180)
    bot.forward(5)
    bot.left(90)
    bot.forward(20)
    user.penup()
    bot.penup()

screen.onkey(up, "Up")
screen.listen()
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

def faster():
    bot.speed(0.0000001)
    bot.color("orange")
    bot.width(4)

def slower():
    bot.speed(1)
    bot.color("pink")
    bot.width(4)

def smaller():
    global trail_size
    if trail_size == 1:
        trailsize = 1
    else:
        trail_size -= 1
        user.width(trail_size)

def larger():
    global trail_size
    trail_size += 1
    user.width(trail_size)

screen.onkey(faster, "z")
screen.listen()
screen.onkey(slower, "x")
screen.listen()
screen.onkey(smaller, "v")
screen.listen()
screen.onkey(larger, "w")
def c_key(): #circle and stamp
    user.dot(size1, color2)
    #c.goto(range1, range2)
    #c.pendown()
    #c.dot(size1, color2)

def r_key(): #rectangle
    #r.penup()
    r.goto(range1, range3)
    user.fillcolor(color3)
    #r.begin_fill()
    #r.pendown()
    #global size1
    #global size2
    global length
    global width
    width = size2
    length = size1
    r.forward(length)
    r.right(90)
    r.forward(width)
    r.right(90)
    r.forward(length)
    r.right(90)
    r.forward(width)
    r.penup()
    r.end_fill()
    user.forward(8)
    bot.write("3 sides only pls", align = "center", font = ("Courier New", 10, "normal"))

def s_key(): #square and "stamp"
    #user.penup()
    #s.goto(range4, range3)
    user.pendown()
    user.fillcolor(color4)
    user.begin_fill()
    global size3
    side = int(size3) #+= 1
    new_side = int(side) #+= 1
    user.forward(side)
    user.right(90)
    user.forward(side)
    user.right(90)
    user.forward(side)
    user.right(90)
    user.forward(side)
    user.end_fill()
    #user.shape("square")

def t_key():  #triangle
    #t.penup()
    #t.fillcolor(color5)
    user.pendown()
    user.fillcolor(color6)
    user.begin_fill()
    user.right(90)
    user.forward(12)
    user.left(135)
    user.forward(15)
    user.left(135)
    user.forward(15)
    user.end_fill()
    user.penup()
    user.forward(12)
    user.pendown()

#minigames:
def quest():
    q1.clear()
    q0.penup()
    q0.goto(-200, -200)
    q0.write("r = rectangle, s = square, c = circle, t = triangle", align = "left", font = ("Courier New", 10, "underline"))
   # if activated == ["one_key()", "game_msg_2())", "c_key()", "r_key()", "s_key()", "t_key()"]:


screen.onkey(c_key, "c")
screen.listen()

screen.onkey(r_key, "r")
screen.listen()

screen.onkey(t_key, "t")
screen.listen()

screen.onkey(s_key, "s")
screen.listen()


def one_key():
    global countdown
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
    quest = "true"

if quest == "true":
    quest()

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
    bot.penup()
    bot.goto(random(x_choices), random(y_choices))
    bot.write("Tag me!", align = "center", font = ("Courier New", 16, "underline"))
    time.sleep(1)
    q2.penup()
    q2.goto(-200, -200)
    q2.fillcolor("black")
    q2.begin_fill()
    q2.forward(200)
    q2.left(90)
    q2.forward(200)
    q2.left(90)
    q2.forward(200)
    q2.left(90)
    q2.forward(200)
    q2.pendown()
    q2.end_fill()
    



screen.onkey(two_key, "2")
screen.listen()

#moved globalized variables from here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!










def a_key(): #spikey triangles
    #a.write("star", align = "center", font = ("Verdana", 15, "normal"))
    time.sleep(sleep)
    #a.clear
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
    global color1
    global color_bank
    #e.write()
    time.sleep(sleep)
    #e.clear()
    e.penup()
    e.fillcolor(color1)
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
    e.fillcolor(color6)
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
