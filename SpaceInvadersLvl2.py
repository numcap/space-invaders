
import turtle, math, random, time

from turtle import*

import tkinter as tk
import tkinter.font as font
from tkinter import*


root = Tk()
root.title ('Space Invaders Level 2')
root.geometry('800x800')
root.configure(bg="black")

def MainMenu():
    root.destroy()
    root.quit()
    import MainMenu

def Restart():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl2

def Quit():
    root.destroy()
    root.quit()

gameMenu= Menu(root)
root.configure(menu=gameMenu)

optionsMenu= Menu(gameMenu)
gameMenu.add_cascade(label= "Options", menu= optionsMenu, font= ("krungthep", 14))
optionsMenu.add_command(label= "Main Menu", command= MainMenu, font= ('krungthep', 14))
optionsMenu.add_separator()
optionsMenu.add_command(label= "Restart Level", command= Restart, font= ('krungthep', 14))
optionsMenu.add_command(label= 'Quit Level', command= root.destroy, font= ('krungthep', 14))



canvas = tk.Canvas(root)
canvas.pack(side=LEFT)
canvas.configure(width=800, height=800, bg= '#011931')

#buttons

btnMainMenu = Button(root, fg='blue', font=('krungthep', 20, 'bold'),
                      text='Main Menu', bg='powder blue', highlightbackground= 'blue', command=MainMenu).place(x=115, y=725)

btnRestart= Button(root, fg='blue', font=('krungthep', 20, 'bold'),
                   text= 'Restart', bg='powder blue', highlightbackground= 'blue', command=Restart).place(x=350, y=725)

btnQuit= Button(root, fg='red', font=('krungthep', 20, 'bold'),
                   text= 'Quit', bg='salmon', highlightbackground= 'red', command=Quit).place(x=565, y=725)

#set up game screen
wn = TurtleScreen(canvas)
wn.bgcolor ('#011931')
wn.bgpic('stars-space1.gif')
wn.tracer (2)
wn.register_shape('spaceship.gif')
wn.register_shape('bullet.gif')
wn.register_shape('invader.gif')

#set up the pen for drawing the border
mypen = turtle.RawTurtle(wn)
mypen.penup()
mypen.hideturtle()
mypen.goto (-350, -280)
mypen.pendown()
mypen.pensize(10)
mypen.color ('blue')

#draw a border 
for side in range (2):
    mypen.forward (700)
    mypen.left (90)
    mypen.forward(550)
    mypen.left(90)

mypen.penup()

#create a player
player = turtle.RawTurtle(wn)
player.color ('white')
player.shape ('spaceship.gif')
player.penup()
player.speed (0)

#create player's bullet
bullets= turtle.RawTurtle(wn)
bullets.shape('bullet.gif')
bullets.penup()
bullets.speed(0)
bullets.setposition(400,-300)
bullets.setheading(90)
bullets.hideturtle()


#create multiple aims using a list
maxAims = 7
aims = []

for count in range (maxAims):
    aims.append(turtle.RawTurtle(wn))
    aims[count].shape ('invader.gif')
    aims[count].penup()
    aims[count].speed(0)
    aims[count].setposition(random.randint (-320, 320), random.randint (-100, 270))

score = 0
speed = 0
bSpeed=15

player.setposition(0,-250)
player.setheading(0)

#define functions
def shoot(canvas):
    bullets.setposition(player.xcor(),player.ycor()+30)
    bullets.showturtle()
    bSpeed= 15

def move_right(canvas):
    global speed
    speed+=4
    if speed>12:
        speed=12
    if speed<0:
        speed=0

def move_left(canvas):
    global speed
    speed-=4
    if speed<-12:
        speed=-12
    if speed>0:
        speed=0

#Keyboard binding
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)
root.bind('<Up>', shoot)


#set up score counter
mypen.setposition(-250, 300)
scorestring = "Score: %s" %score
mypen.write (scorestring, False, align= "center", font=("krungthep", 25))

#set up lives counter 
lives=3
deathPen = turtle.RawTurtle(wn)
deathPen.color('blue')
deathPen.penup()
deathPen.setposition(0,300)
deathPen.pendown()
deathstring = "Lives: %s" %lives
deathPen.write (deathstring, False, align= "center", font=("krungthep",25))
deathPen.hideturtle()

staticPen = turtle.RawTurtle(wn)
staticPen.color('blue')
staticPen.penup()
staticPen.setposition(250, 300)
staticPen.pendown()
staticPen.write('Level 2', False, align= "center", font=("krungthep", 25))
staticPen.penup()
staticPen.hideturtle()

#Intro
introPen = turtle.RawTurtle(wn)
introPen.color('blue')
introPen.fillcolor('blue')
introPen.hideturtle()
introPen.penup()
introPen.setposition(-350,-25)
introPen.begin_fill()
introPen.pendown()
for i  in range (2):
    introPen.forward(700)
    introPen.left(90)
    introPen.forward(100)
    introPen.left(90)
introPen.end_fill()
introPen.penup()
#Intro
introPen.color("white")
introPen.setposition(0,0)
introPen.write("Level 2", False, align="center", font=("krungthep", 40))
time.sleep(2)
introPen.clear()



while True:


    player.forward(speed)
    bullets.forward(bSpeed)

    if player.xcor() > 320 or player.xcor() < -320:
        player.setposition(0,-250)
        speed=0
        time.sleep(1)
        lives-=1
        #Draw the lives on the screen
        deathPen.clear()
        deathstring = "Lives: %s" %lives
        deathPen.write (deathstring, False, align= "center", font=("krungthep",25))
        deathPen.hideturtle()

    if lives==0:
        introPen.setposition(100,0)
        introPen.color('blue')
        introPen.fillcolor('blue')
        introPen.hideturtle()
        introPen.penup()
        introPen.setposition(-350,-25)
        introPen.begin_fill()
        introPen.pendown()
        for i  in range (2):
            introPen.forward(700)
            introPen.left(90)
            introPen.forward(100)
            introPen.left(90)
        introPen.end_fill()
        introPen.penup()
        introPen.color("white")
        introPen.setposition(0,0)
        introPen.write("Game Over", False, align="center", font=("krungthep", 40))
        time.sleep(3)
        root.destroy()
        root.quit()
        import MainMenu
        
            


    #move all aims
    for count in range(maxAims):
        
        aims[count].forward(8.5)

        if  aims[count].xcor() < -330:
            aims[count].left(90)
            aims[count].forward(20)
            aims[count].left(90)
        elif aims[count].xcor() > 325 :
             aims[count].right(90)
             aims[count].forward(20)
             aims[count].right(90)

     


        d = math.sqrt(math.pow(bullets.xcor() - aims[count]. xcor(), 2) + math.pow(bullets.ycor() - aims [count].ycor(),2))
        dLives = math.sqrt(math.pow(player.xcor() - aims[count]. xcor(), 2) + math.pow(player.ycor() - aims [count].ycor(),2))

        if bullets.ycor() > 260:
            bullets.hideturtle()
            bullets.setposition(360,-300)

        if dLives < 50:
            aims[count].hideturtle()
            aims[count].setposition(-300, -300)
            lives -=1
            deathPen.clear()
            deathstring = "Lives: %s" %lives
            deathPen.write (deathstring, False, align= "center", font=("krungthep",25))
            deathPen.hideturtle()
            
            
        if d < 30:
            aims[count].hideturtle()
            aims[count].setposition(-300, -300)
            score +=1
            bullets.hideturtle()
            bullets.setposition(400,-400)
            
            #Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-250, 300)
            scorestring = "Score: %s" %score
            mypen.write (scorestring, False, align= "center", font=("krungthep", 25))


        if score == 7:
            time.sleep(3)
            root.quit()
            root.destroy()
            import SpaceInvadersLvl3
            
            
            
        
