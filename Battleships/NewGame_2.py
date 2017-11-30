from Functions import *
from Tkinter import *
import os
window2=Tk()
window2.config(bg="lightblue") #will set the background of window to light blue.
window2.title("BATTLESHIPS")#will give the title to window as BATTLESHIPS.

topFrame=Frame(window2)# creates a top frame.
topFrame.config(bg="lightblue")
topFrame.pack(side=TOP,fill=X)

title=Label(topFrame,text="BATTLESHIPS",bg="black",fg = "white")#will set the title to BATTLESHIPS.
title.config(font=200)#sets the size of the text to 200.
title.pack(side=TOP)

label1=Label(topFrame)
label1.config(width=25,bg="lightblue")
label1.pack(side=TOP)

label2=Label(topFrame,text="PLAYER 1 TERRITORY",fg="green")#adds text as PLAYER 1 TERRITORY
label2.config(font=50,width=20)					#fg sets the text colour to green
label2.pack(side=LEFT)

blank=Label(topFrame)#adds a blank label to create gap.
blank.config(width=10,font=50,bg="lightblue")#width sets the width of the label as 30.
blank.pack(side=RIGHT,fill=X)

label3=Label(topFrame,text="PLAYER 2 TERRITORY",fg="green")#adds text as PLAYER 2 TERRITORY
label3.config(font=50,width=20)
label3.pack(side=RIGHT)

rightFrame=Frame(window2)
rightFrame.config(bg="lightblue")
leftFrame=Frame(window2)
leftFrame.config(bg="lightblue")

user1frame=Frame(leftFrame)
user1frame.config()
user1Grid=[]
#to create a 10X10 grid with buttons
for j in range(10):
    Brow=[]
    for i in range(10):
        b=Button(user1frame,bg="blue")
        b.config(height=1,width=2)
        b.grid(row=j,column=i)
        Brow.append(b)
    user1Grid.append(Brow)
user1frame.pack(side=LEFT)

user2frame=Frame(rightFrame)
user2frame.config()
user2Grid=[]
#to create a 10X10 grid with buttons
for j in range(10):
    Brow=[]
    for i in range(10):
        b=Button(user2frame,bg="blue")
        b.config(height=1,width=2)
        b.grid(row=j,column=i)
        Brow.append(b)
    user2Grid.append(Brow)
user2frame.pack(side=LEFT)
def quit():#quits the game
    window2.destroy()
def newgame():#pressing the button starts a new game
    cmd="python NewGame_1.py"#links the newgame button to NewGame_1.py file
    f=os.popen(cmd)
    quit()
newgamebutton=Button(text="New Game",bg="red",command = newgame)#creates a new game button
quitbutton=Button(text="Quit",bg="red",command=quit)#creates an about button

quitbutton.config(height=2,width=10,font=25)
quitbutton.pack(side=BOTTOM)



newgamebutton.config(height=2,width=10,font=25)
newgamebutton.pack(side=BOTTOM)

bottomFrame=Frame(window2,height=50,width=60)
bottomFrame.config(bg="lightblue")
label4=Label(topFrame,text="")
label4.config(bg="lightblue",font=45,width=50)
label4.pack(side=TOP)
label10=Label(topFrame,text="")
label10.config(bg="lightblue",font=45,width=50)
label10.pack(side=TOP)
leftFrame.config(height=30)
rightFrame.config(height=30)

gap1=Label(window2,bg="lightblue")
gap1.config(width=30,height=40)

user1=User1(user1Grid, label4, label10)
user2=User2(user2Grid,label4, label10)




leftFrame.pack(side=LEFT)#creates a leftframe in window
gap1.pack(side=LEFT)
rightFrame.pack(side=RIGHT)#creates a rightframe in window

bottomFrame.pack(side=BOTTOM,fill=X)#creates a bottom frame in window


window2.mainloop()
