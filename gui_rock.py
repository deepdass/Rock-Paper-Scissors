import random  
from tkinter import *

x = "rock"
y = "paper"
z ="scissor"

def choice(b):
    a = ["rock","paper","scissor"]
    c = random.choice(a)
    comp.config(text="Computer choose : " + str(c))

    if b == c:
        win.config(text="Draw") 
    
    if c == z and b == y:
        win.config(text="Computer win") 
    if c == y and b == x:
        win.config(text="Computer win") 
    if c ==x and b == z:
        win.config(text="Computer win") 


    if c == y and b == z:
        win.config(text="Player win")
    if c == x and b == y:
        win.config(text="Player win")
    if c ==z and b==x:
        win.config(text="Player win")
            
w = Tk()

comp=Label(w,text="Computer choose : " )
comp.grid(row=0,column=0,columnspan=3)

rock = Button(w,text="Rock",relief=FLAT,command= lambda: choice("rock"))
rock.grid(row=1,column=0)

paper = Button(w,text="paper",relief=FLAT,command= lambda: choice("paper"))
paper.grid(row=1,column=1)

scissor = Button(w,text="scissor",relief=FLAT,command= lambda: choice("scissor"))
scissor.grid(row=1,column=2)

win=Label(w,text="")
win.grid(row=2,column=0,columnspan=3)

w.mainloop()
