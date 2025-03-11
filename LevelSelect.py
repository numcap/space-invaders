
import tkinter as tk
import tkinter.font as font
from tkinter import*

import turtle
from turtle import*

root= Tk()
root.title ('Space Invaders')
root.geometry('800x800')
root.configure(bg='blue')

canvas = tk.Canvas(root)
canvas.pack(side=LEFT)
canvas.configure(width=800, height=800, bg='#011931')

wn = TurtleScreen(canvas)
wn.bgpic('blackscreen.gif')
wn.tracer(2)

levelselectPen = turtle.RawTurtle(wn)
levelselectPen.color('white')
levelselectPen.hideturtle()
levelselectPen.penup()
levelselectPen.setposition(0, 200)
levelselectPen.write("Level Select", align='center', font=('krungthep', 50, 'bold'), )


#define levels
def Level1():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl1

def Level2():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl2

def Level3():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl3

def Level4():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl4

def Level5():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl5

def Back():
    root.destroy()
    root.quit()
    import MainMenu
    

#buttons for the levels
btnLvl1= Button(root, padx= 35, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Level 1', bg='powder blue', highlightbackground= 'blue', command=Level1).place(x=150,y=250)

btnLvl2 = Button(root, padx= 35, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Level 2', bg='powder blue', highlightbackground= 'blue', command=Level2).place(x=150,y=350)

btnLvl3 = Button(root, padx= 35, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Level 3', bg='powder blue', highlightbackground= 'blue', command=Level3).place(x=150,y=450)

btnLvl4= Button(root, padx= 35, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Level 4', bg='powder blue', highlightbackground= 'blue', command=Level4).place(x=150,y=550)

btnLvl5 = Button(root, padx= 35, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Level 5', bg='powder blue', highlightbackground= 'blue', command=Level5).place(x=150,y=650)

btnBack = Button(root, padx= 25, pady= 40, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Back', bg='powder blue', highlightbackground= 'blue', command=Back).place(x=500,y=435)





