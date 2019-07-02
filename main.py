from turtle import *
import random

#TODO 02 June 2019 :
#1. test destroy method of obstacle √
#2. add win method for objectif
#3. test it
#4. set lvl design

#=====BACKEND=====
posspos = [[i,j] for i in range(-240,260,10) for j in range(-150,160,10)]

#screen setup
wn = Screen()
wn.bgcolor("Black")
wn.title("GoodZilla")
wn.setup(600,400)

score = Turtle()
score.hideturtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0,150)
score.pendown()
score.write(100)

#player
class Player(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.x = -250
        self.y = 0
        self.w = 20
        self.h = 40
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=4,stretch_len=2)
        self.penup()
        self.goto(self.x,self.y)
        self.color("blue")
        self.score = 100

    #control methods
    def goup(self):
        self.sety(self.ycor() + 5)

    def godown(self):
        self.sety(self.ycor() - 5)

    def goright(self):
        self.setx(self.xcor() + 5)


#mère batiment
class Building(Turtle):
    def __init__(self,x,y):
        Turtle.__init__(self)
        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
        self.shape("square")
        self.speed(0)
        self.penup()
        self.goto(self.x,self.y)

#fille obstacle
class Obstacle(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.color("white")

    def destroy(self,p):
        #destroy obstacle if player hit
        #input : Player obj
        #output : none
        if ((abs(self.ycor() - p.ycor()) < 55) and abs(self.xcor()-p.xcor()) < 35):
            self.hideturtle()
            p.score -= 5
            score.clear()
            score.write(p.score)
            self.goto(1000,1000)

#fille centrale
class Objectif(Building):
    def __init__(self):
        Building.__init__(self,250,0)
        self.color("red")
    
    def Win(self,p):
        #change color and end the game if player reach it
        #input : Player obj
        #output : bool
        if ((abs(self.ycor() - p.ycor()) < 55) and abs(self.xcor()-p.xcor()) < 35):
            self.color("green")
            return True
        else:
            return False

pos = []
for i in range(20):
    a = random.choice(posspos)
    pos.append(a)

#=====FRONTEND=====
#create objects
obs = []
for k in pos:
    obs.append(Obstacle(k[0],k[1]))

p = Player()
c = Objectif()

#player control
listen()
onkey(p.goup,"Up")
onkey(p.godown,"Down")
onkey(p.goright,"Right")

while not c.Win(p):
    wn.update()
    for o in obs:
        o.destroy(p)

print("Your final score is",p.score)

wn.bye()
