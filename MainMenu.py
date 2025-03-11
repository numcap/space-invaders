

import time

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
wn.register_shape('space-invaders.gif')
wn.bgpic('blackscreen.gif')
wn.tracer(2)


mainImage = turtle.RawTurtle(wn)
mainImage.penup()
mainImage.setposition(0,200)
mainImage.shape('space-invaders.gif')
mainImage.showturtle()


coinPenBorder = turtle.RawTurtle(wn)
coinPenBorder.color('black')
coinPenBorder.fillcolor('black')
coinPenBorder.hideturtle()
coinPenBorder.penup()
coinPenBorder.setposition(-350,-100)
coinPenBorder.begin_fill()
coinPenBorder.pendown()
for i  in range (2):
    coinPenBorder.forward(700)
    coinPenBorder.left(90)
    coinPenBorder.forward(100)
    coinPenBorder.left(90)
coinPenBorder.end_fill()
coinPenBorder.penup()

coinPen = turtle.RawTurtle(wn)
coinPen.color("white")
coinPen.hideturtle()
coinPen.penup()
coinPen.setposition(0,-50)
for n in range (0,3):
    coinPen.write("INSERT COIN", False, align="center", font=("krungthep", 40))
    time.sleep(0.5)
    coinPen.clear()
    time.sleep(0.5)
coinPenBorder.clear()

def Start():
    root.destroy()
    root.quit()
    import SpaceInvadersLvl1

def Quit():
    root.destroy()
    root.quit()

def LevelSelect():
    root.destroy()
    root.quit()
    import LevelSelect

#buttons
btnStart= Button(root, padx= 30, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Start', bg='powder blue', highlightbackground= 'blue', command=Start).place(x=325,y=400)

btnQuit = Button(root, padx= 35, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Quit', bg='powder blue', highlightbackground= 'blue', command=Quit).place(x=325,y=600)

btnLvlSelect = Button(root, padx= 33, pady= 15, bd=0,  fg='blue', font=('krungthep', 20, 'bold'),
            text='Level Select', bg='powder blue', highlightbackground= 'blue', command=LevelSelect).place(x=285,y=500)






