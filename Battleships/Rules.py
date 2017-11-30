from Tkinter import *
windowR = Tk()
windowR.title("Rules")
logo = PhotoImage(file="SeaStar.png")

rules = "Welcome to Battleships!\nBattleships is a two player game where players can place 'ships' in a 10x10 grid . The aim of the game is to destroy all of the opponent's ships.\nThere is:\n 1 AIRCRAFT CARRIER (5 BLOCKS)\n1 SUBMARINE (4 BLOCKS)\n1 BATTLESHIP (3 BLOCKS)\n2 DESTROYERS (2 BLOCKS)\n2 PATROL SHIPS (1 BLOCK).\nRules:\n(i) Ships are placed randomly in the 10x10 grid.\n(ii) Ships are only placed vertically or horizontally and do not overlap.\n(iii) This is a turn based game where players call co-ordinates on the grid where they think the opponent's ships might be and are informed whether their call is a hit or a miss.\n(iv) When a co-ordinate is called, a red coloured box signifies a hit and a yellow coloured box signifies a miss.\n(v) The first player to destroy all of the opponent's ships is the winner."

w = Label(windowR,compound = CENTER,text=rules,image=logo, fg = 'red')
w.pack(side="right")
windowR.mainloop()
