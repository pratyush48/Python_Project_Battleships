from Tkinter import *
import os # basically the module to connect the program to the command line.

window1 = Tk()
window1.title("BATTLESHIPS")#Title is added to window.
set_the_picture=Canvas(window1,height = 800,width = 1250)
set_the_picture.pack(expand = True, fill = BOTH)
#To add image as a background to window. 
image_of_ship=PhotoImage(file = "battleship.png")
set_the_picture.create_image(0, 0,anchor = NW,image = image_of_ship)
def TO_START_CLICK_HERE(): # on pressing the button, this method is called, which starts the game.
    cmd = "python NewGame_1.py"
    file = os.popen(cmd) # command to open given file by typing on command line
    pygame.quit() #once 'Ready for battle?' is clicked, the music stops.
    quit()
    window1.destroy()
def RULES():
    cmd = "python Rules.py"
    file = os.popen(cmd)
def ABOUT():#pressing the button open the about window 
    cmd = "python About.py"
    f = os.popen(cmd)
rules_button=Button(set_the_picture,text="RULES",bg="red",fg = "black",font = 100,command = RULES)#creates a Rules button
about_button=Button(set_the_picture,text="ABOUT",bg="red",fg = "black",font = 100,command = ABOUT)#creates a About button
ready_for_battle_button = Button(set_the_picture,text = "READY FOR BATTLE ?",bd = 0,bg = "red",fg = "black",font = 100,command = TO_START_CLICK_HERE)#creates a START GAME button.
ready_for_battle_button.pack(side = BOTTOM)
about_button.pack(side = BOTTOM)
rules_button.pack(side = BOTTOM)
# next three lines superpose the buttons on the image without creating a separate frame.
set_the_picture.create_window(50,600,window = ready_for_battle_button, anchor = NW)
set_the_picture.create_window(600,600,window = about_button, anchor = NW)
set_the_picture.create_window(1100,600,window = rules_button, anchor = NW)
import pygame # only used for background music.
file = 'got.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
window1.mainloop()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

